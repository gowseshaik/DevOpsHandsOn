FROM docker.io/store/oracle/database-enterprise:12.2.0.1

ENV DB_SID=SBLDB
    ## db passwd
    ## default : Oracle
ENV DB_PASSWD=Oracle
    ## db domain
    ## default : localdomain
ENV DB_DOMAIN=localdomain
    ## db bundle
    ## default : basic
    ## valid : basic / high / extreme 
    ## (high and extreme are only available for enterprise edition)
ENV DB_BUNDLE=basic=value

VOLUME SBL-u01:/u01
VOLUME SBL-u02:/u02
VOLUME SBL-u03:/u03
VOLUME SBL-u04:/u04

EXPOSE 1521:1521
EXPOSE 5500:5500


