import java.io.FileOutputStream
import java.io.IOException
import java.util.Properties
import org.gradle.api.DefaultTask
import org.gradle.api.file.RegularFileProperty
import org.gradle.api.provider.Property
import org.gradle.api.tasks.Input
import org.gradle.api.tasks.OutputFile
import org.gradle.api.tasks.TaskAction

abstract class BuildInfo : DefaultTask() {
    @get:Input
    abstract val version: Property<String?>

    @get:OutputFile
    abstract val outputFile: RegularFileProperty
    @TaskAction
    @Throws(IOException::class)
    fun create() {
        val prop = Properties()
        prop.setProperty("version", version.get())
        FileOutputStream(outputFile.asFile.get()).use { output -> prop.store(output, null) }
    }
}
