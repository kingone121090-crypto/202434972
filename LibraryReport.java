package example.library;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import org.apache.commons.text.StringEscapeUtils;

/** A toy reporting class; this project is NOT intended to be built/deployed. */
public final class LibraryReport {
    private static final Logger LOGGER = LogManager.getLogger(LibraryReport.class);

    private LibraryReport() { }

    public static String printableTitle(String title) {
        String safeTitle = StringEscapeUtils.escapeHtml4(title);
        LOGGER.info("Generated dummy library report");
        return safeTitle;
    }
}
