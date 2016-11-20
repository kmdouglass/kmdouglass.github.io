<!-- 
.. title: Fiji
.. slug: fiji
.. date: 2016-07-29 10:04:25 UTC+02:00
.. tags: Fiji
.. category: 
.. link: 
.. description: Notes on using and developing Fiji.
.. type: text
-->

# Setup the FIJI Development Environment

- The guide on setting up the development environment is here:
  [http://imagej.net/Developing_ImageJ_in_Eclipse#Create_the_Eclipse_Projects](http://imagej.net/Developing_ImageJ_in_Eclipse#Create_the_Eclipse_Projects)

- Be sure to download Eclipse for Java Developers, not Eclipse for
  Java EE Developers.

- Start plugin development by cloning the minimal IJ1 plugin and
  importing it into Eclipse:
  [https://github.com/imagej/minimal-ij1-plugin/](https://github.com/imagej/minimal-ij1-plugin/)
  Import it as an existing Maven project.

- The **README.md** file from the minimal IJ1 plugin is very useful
  for instructions on setting up the environment.

- To ensure that Maven is aware of the Fiji directory, select *Run >
  Run Configurations...* In the new window, double click **Maven
  Build** and to create a new configuration. The name should match
  your project. Add the following parameter: name:
  `imagej.app.directory` value: `/home/douglass/src/Fiji.app`

- To build the plugin, select Run As... and select Maven build. You
  might have to specify the `imagej.app.directory` here if it wasn't
  set correctly in the step above. Even then, it didn't find the app
  directory and and instead wrote the .jar file to the target
  directory. The second time with some fuss I managed to get it
  working.

- **Don't use the jdk1.6.0_24 that comes with Fiji**. Maven builds
  fail with an unsupported version error when I use it.

## Maven and Plugin Dependencies

- The ImageJ Maven repository is at http://maven.imagej.net/

- When adding dependencies, first search the repository for the name
  of your package. More information on finding Maven packages is here:
  http://imagej.net/Maven#How_to_find_a_dependency.27s_groupId.2FartifactId.2Fversion_.28GAV.29.3F

- To add a Maven dependency, you add the package information between
  the `<dependencies>` tags inside your plugin's *pom.xml* file. These
  tags can be copied from the Maven repository website by clicking on
  the package name and inspecting the XML code in the frame containing
  the **Maven** and **Artifact** tabs. For example, the XML for the
  jhdf5 package that is used by the HDF5 Plugin is

```
<dependency>
  <groupId>ch.systems.cisd</groupId>
  <artifactId>jhdf5</artifactId>
  <version>14.12.0</version>
</dependency>
```

- When adding a package, you should also verify whether Maven is aware
  of the package's repository. For example, the jhdf5 package exists
  in the **OME External** repository, which was not found until I
  explictly added the **imagej.public** repository to my *pom.xml*
  file. See
  http://forum.imagej.net/t/adding-ij-maven-repository-to-pom-xml/199
  for more information.

```
<repositories>
 <repository>
   <id>imagej.public</id>
   <url>http://maven.imagej.net/content/groups/public</url>
 </repository>
</repositories>
```

# Useful Links

[http://forum.imagej.net/t/creation-of-a-new-plug-in-in-eclipse-beginners-question/2008](http://forum.imagej.net/t/creation-of-a-new-plug-in-in-eclipse-beginners-question/2008)

# Eclipse Setup (Didn't work)

## Use FIJI's JRE

When creating a new project in Eclipse, we can set the JRE to the same
one used by FIJI. To do so, select **Configure JREs** inside the *New
Java Project* window. Then, click the **Search...** button and look
search inside **Fiji.app/java**.

When I did this, it found the jdk1.6.0_24 JRE. Once selecting OK,
return to the **New Java Project** window and select the radio button
next to **Use a project specific JRE:**. Be sure to choose the
jdk1.6.0_24 JRE that was just found.

## Link Additional Source

In the window *New Java Project > Java Settings* I linked an
additional source: the folder **Fiji.app/jars**.
