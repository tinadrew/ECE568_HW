<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform" xmlns:msxsl="urn:schemas-microsoft-com:xslt" exclude-result-prefixes="msxsl">

<xsl:template match="/">
<html>
  <head>
  	<title>Bibliography</title>
  </head>
  <body background="antiquewhite">
    <center><h2>Bibliography</h2><hr width="90%"/></center>
    <ul>
      <xsl:for-each select="bib/book">
        <li>
          <xsl:value-of select="./author/last/text()"/><xsl:text>, </xsl:text>
          <xsl:value-of select="./author/first/text()"/><xsl:text>. </xsl:text>
          <b><xsl:value-of select="./title/text()"/></b><xsl:text> (</xsl:text> 
          <xsl:value-of select="./publisher/text()"/><xsl:text> </xsl:text>
          <xsl:value-of select="./year/text()"/><xsl:text>).</xsl:text>
        </li>
      </xsl:for-each>
      <xsl:for-each select="bib/article">
 
        <li>
		  <xsl:value-of select="./author/last/text()"/><xsl:text>, </xsl:text>
          <xsl:value-of select="./author/first/text()"/><xsl:text>. </xsl:text>
          <xsl:value-of select="title/text()"/><xsl:text>. </xsl:text>
          <b><xsl:value-of select="journal/text()"/><xsl:text>, </xsl:text>
          <xsl:value-of select="volume/text()"/></b><xsl:text>, </xsl:text>
          <xsl:text>pp. </xsl:text>
          <xsl:value-of select="page/from/text()"/><xsl:text>-</xsl:text>
          <xsl:value-of select="page/to/text()"/><xsl:text>, </xsl:text>
          <xsl:value-of select="year"/><xsl:text>.</xsl:text>
        </li>
      </xsl:for-each>
    </ul>
  </body>
</html>

</xsl:template>
<xsl:template match="page">
<xsl:value-of select="from"/>-<xsl:value-of select="to"/>,
</xsl:template>
</xsl:stylesheet>