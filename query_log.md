```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen FROM women_stemDB GROUP BY Major ORDER BY SumTotal DESC LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7017725, SumWomen=4223675), Row(Major='NURSING', SumTotal=5234850, SumWomen=4690525), Row(Major='COMPUTER SCIENCE', SumTotal=3207975, SumWomen=714400), Row(Major='MECHANICAL ENGINEERING', SumTotal=2280675, SumWomen=272675), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2038175, SumWomen=400400), Row(Major='MATHEMATICS', SumTotal=1809925, SumWomen=811025), Row(Major='CHEMISTRY', SumTotal=1663250, SumWomen=840175), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1551300, SumWomen=875925), Row(Major='GENERAL ENGINEERING', SumTotal=1528800, SumWomen=386725), Row(Major='CIVIL ENGINEERING', SumTotal=1328825, SumWomen=301800)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7298434, SumWomen=4392622), Row(Major='NURSING', SumTotal=5444244, SumWomen=4878146), Row(Major='COMPUTER SCIENCE', SumTotal=3336294, SumWomen=742976), Row(Major='MECHANICAL ENGINEERING', SumTotal=2371902, SumWomen=283582), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2119702, SumWomen=416416), Row(Major='MATHEMATICS', SumTotal=1882322, SumWomen=843466), Row(Major='CHEMISTRY', SumTotal=1729780, SumWomen=873782), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1613352, SumWomen=910962), Row(Major='GENERAL ENGINEERING', SumTotal=1589952, SumWomen=402194), Row(Major='CIVIL ENGINEERING', SumTotal=1381978, SumWomen=313872)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=7579143, SumWomen=4561569), Row(Major='NURSING', SumTotal=5653638, SumWomen=5065767), Row(Major='COMPUTER SCIENCE', SumTotal=3464613, SumWomen=771552), Row(Major='MECHANICAL ENGINEERING', SumTotal=2463129, SumWomen=294489), Row(Major='ELECTRICAL ENGINEERING', SumTotal=2201229, SumWomen=432432), Row(Major='MATHEMATICS', SumTotal=1954719, SumWomen=875907), Row(Major='CHEMISTRY', SumTotal=1796310, SumWomen=907389), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=1675404, SumWomen=945999), Row(Major='GENERAL ENGINEERING', SumTotal=1651104, SumWomen=417663), Row(Major='CIVIL ENGINEERING', SumTotal=1435131, SumWomen=325944)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen FROM women_stemDB GROUP BY Major ORDER BY SumTotal DESC LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=13754741, SumWomen=8278403), Row(Major='NURSING', SumTotal=10260306, SumWomen=9193429), Row(Major='COMPUTER SCIENCE', SumTotal=6287631, SumWomen=1400224), Row(Major='MECHANICAL ENGINEERING', SumTotal=4470123, SumWomen=534443), Row(Major='ELECTRICAL ENGINEERING', SumTotal=3994823, SumWomen=784784), Row(Major='MATHEMATICS', SumTotal=3547453, SumWomen=1589609), Row(Major='CHEMISTRY', SumTotal=3259970, SumWomen=1646743), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=3040548, SumWomen=1716813), Row(Major='GENERAL ENGINEERING', SumTotal=2996448, SumWomen=757981), Row(Major='CIVIL ENGINEERING', SumTotal=2604497, SumWomen=591528)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=14035450, SumWomen=8447350), Row(Major='NURSING', SumTotal=10469700, SumWomen=9381050), Row(Major='COMPUTER SCIENCE', SumTotal=6415950, SumWomen=1428800), Row(Major='MECHANICAL ENGINEERING', SumTotal=4561350, SumWomen=545350), Row(Major='ELECTRICAL ENGINEERING', SumTotal=4076350, SumWomen=800800), Row(Major='MATHEMATICS', SumTotal=3619850, SumWomen=1622050), Row(Major='CHEMISTRY', SumTotal=3326500, SumWomen=1680350), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=3102600, SumWomen=1751850), Row(Major='GENERAL ENGINEERING', SumTotal=3057600, SumWomen=773450), Row(Major='CIVIL ENGINEERING', SumTotal=2657650, SumWomen=603600)]
```

```sql
SELECT Major, SUM(Total) as SumTotal, SUM(Women) as SumWomen 
            FROM women_stemDB 
            GROUP BY Major 
            ORDER BY SumTotal DESC 
            LIMIT 10
```

```response from databricks
[Row(Major='BIOLOGY', SumTotal=14316159, SumWomen=8616297), Row(Major='NURSING', SumTotal=10679094, SumWomen=9568671), Row(Major='COMPUTER SCIENCE', SumTotal=6544269, SumWomen=1457376), Row(Major='MECHANICAL ENGINEERING', SumTotal=4652577, SumWomen=556257), Row(Major='ELECTRICAL ENGINEERING', SumTotal=4157877, SumWomen=816816), Row(Major='MATHEMATICS', SumTotal=3692247, SumWomen=1654491), Row(Major='CHEMISTRY', SumTotal=3393030, SumWomen=1713957), Row(Major='MULTI-DISCIPLINARY OR GENERAL SCIENCE', SumTotal=3164652, SumWomen=1786887), Row(Major='GENERAL ENGINEERING', SumTotal=3118752, SumWomen=788919), Row(Major='CIVIL ENGINEERING', SumTotal=2710803, SumWomen=615672)]
```

