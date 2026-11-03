---
content_hash: b1eea2d1ab7054c9306c6f38ae634c17e1aa6d1fc153f9a240d0a4107cd60bd9
fetched_at: '2026-06-29T00:08:35.571236+00:00'
page_id: '281982359'
product: rm
source: tdn-rm
title: BD0026_Nível_de_Compatibilidade_SQL_Server_2016_(130)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=281982359
version: 9
---

```
Assunto
```

|  |  |
| --- | --- |
| **Produto:** | Banco de Dados |
| **Versões:** | 12.1.17 |
| **Ocorrência:** | Bloqueio de Atualização de Versão no nível de compatibilidade SQL Server 2016 (130) |
| **Ambiente:** | RM |

**Devido a mudança de comportamento na quebra para conversão de formatos de data, o produto RM não permitirá o uso do nível de compatibilidade (130) disponível no SQL Server 2016 e Azure SQL Database. **Os aplicativos afetados podem usar um nível de compatibilidade de banco de dados antecedentes ao SQL Server 2016 ( 100 | 110 | 120) até a que as adequações necessárias sejam realizada nas versões futuras do RM.**Abaixo discorremos a respeito do fato impeditivo para esta alteração.**

Em suma, a conversão de data e hora para um tipo de dados temporais de maior precisão (datetime2, datetimeoffset ou time) pode render um valor de tempo diferente, porem mais preciso, do que em versões anteriores. Além disso, os atributos envolvendo datetime consideram a precisão total do valor interno do datatime cheio ao invés do valor do tempo arredondado para o milissegundo mais próximo. Essas mudanças no comportamento de conversão e comparação podem afetar aplicativos existentes e não são intuitivas, a menos que se entenda a fundo a implementação  do tipo de dado datetime.

**Versões Antecedentes ao SQL Server 2016**  
 Você pode estar ciente de que a precisão do tempo da data é limitada a 1/300 de segundo. Isso ocorre porque os valores são internamente uma estrutura de 8 bytes consistindo em 2 inteiros separados de 32 bits, um com o número de unidades de dia desde 1900-01-01 e o outro com o número de unidades de intervalo de 1/300 segundo desde a meia-noite. O intervalo de unidade do 1/300 segundo limita a precisão do tempo a 3.33333 ... milissegundos e o valor de milissegundos será um decimal repetido quando as unidades do intervalo de tempo não são divisíveis uniformemente em 3. O valor decimal cheio é arredondado para uma escala de 3 de acordo com o Precisão de data / hora fixa de 3, resultando em um milissegundo de 0, 3 ou 7 para todos os valores de data e hora.

**Comportamento**  
 Antes do SQL Server 2016, a conversão de data e hora para outro tipo temporal usou o valor do datatime de origem depois que foi arredondado para o milissegundo mais próximo, o qual truncou milissegundos fracos decimais repetidos. O valor arredondado foi então arredondado novamente de acordo com a precisão do tipo de destino. Quando a precisão do tipo de destino foi maior do que 3, o tempo foi estendido para a precisão do tipo de destino com zeros à esquerda insignificantes, resultando em zero para o valor de sub-milissegundo.

| --Este Script altera o níveis de compatibilidade para as versões anteriores ALTER DATABASE database\_name SET COMPATIBILITY\_LEVEL = { 80 | 90 | 100 | 110 | 120 } GO DECLARE @DateTime datetime = '2016-01-01T00:00:00.007'; SELECT CAST(@DateTime AS datetime2(0)); --2016-01-01 00:00:00 SELECT CAST(@DateTime AS datetime2(1)); --2016-01-01 00:00:00.0 SELECT CAST(@DateTime AS datetime2(2)); --2016-01-01 00:00:00.01 SELECT CAST(@DateTime AS datetime2(3)); --2016-01-01 00:00:00.007 SELECT CAST(@DateTime AS datetime2(4)); --2016-01-01 00:00:00.0070 SELECT CAST(@DateTime AS datetime2(5)); --2016-01-01 00:00:00.00700 SELECT CAST(@DateTime AS datetime2(6)); --2016-01-01 00:00:00.007000 SELECT CAST(@DateTime AS datetime2(7)); --2016-01-01 00:00:00.0070000 |
| --- |

Além disso, quando o tempo da data foi comparado com outro tipo temporal, o valor arredondado foi usado. Este script mostra que o resultado do predicado de igualdade é verdadeiro depois que o valor de data e hora é convertido em datetime2.

| --Este Script altera o nível de compatibilidade para as versões anteriores ALTER DATABASE database\_name SET COMPATIBILITY\_LEVEL = { 80 | 90 | 100 | 110 | 120 } GO --Este script imprime o predicado IGUAL é verdadeiro DECLARE @DateTime datetime = '2016-01-01T00:00:00.003'; DECLARE @DateTime2 datetime2(7) = @DateTime; IF @DateTime = @DateTime2 PRINT 'A igualdade entre @DateTime e @DateTime2 é verdadeira' ELSE PRINT 'A igualdade entre @DateTime e @DateTime2 não é verdadeira'; IF @DateTime < @DateTime2 PRINT 'O @DateTime é menor que o @DateTime2' ELSE PRINT 'O @DateTime não é menor que o @DateTime2'; IF @DateTime > @DateTime2 PRINT 'O @DateTime é maior que o @DateTime2' ELSE PRINT 'O @DateTime não é maior que o @DateTime2'; GO --Este script imprime o predicado IGUAL é verdadeiro DECLARE @DateTime datetime = '2016-01-01T00:00:00.007'; DECLARE @DateTime2 datetime2(7) = @DateTime; IF @DateTime = @DateTime2 PRINT 'A igualdade entre @DateTime e @DateTime2 é verdadeira' ELSE PRINT 'A igualdade entre @DateTime e @DateTime2 não é verdadeira'; IF @DateTime < @DateTime2 PRINT 'O @DateTime é menor que o @DateTime2' ELSE PRINT 'O @DateTime não é menor que o @DateTime2'; IF @DateTime > @DateTime2 PRINT 'O @DateTime é maior que o @DateTime2' ELSE PRINT 'O @DateTime não é maior que o @DateTime2'; GO |
| --- |

**Alteração de comportamento do SQL Server 2016**

O SQL Server 2016 e Azure SQL Database V12 usam o valor interno do datetime cheio sem arredondamento durante a conversão para outro tipo temporal. O valor é arredondado apenas uma vez durante a conversão, para a precisão do tipo de destino. O resultado final será o mesmo que antes do SQL Server 2016 quando a precisão do tipo de destino for 3 ou menos. No entanto, o valor convertido será diferente quando a precisão do tipo de destino for maior do que 3 e o intervalo da unidade de tempo interno não é divisível uniformemente em 3 (ou seja, o valor do milissegundo da data da fonte arredondada é 3 ou 7). Observe os microssegundos e nanossegundos não-zero nos resultados do script abaixo e que o arredondamento é baseado na precisão do tipo de destino em vez da fonte.

| --Este Script altera o nível de compatibilidade para as versão do SQL Server 2016 ALTER DATABASE database\_name SET COMPATIBILITY\_LEVEL = 130 DECLARE @DateTime datetime = '2016-01-01T00:00:00.003'; SELECT CAST(@DateTime AS datetime2(0)); --2016-01-01 00:00:00 SELECT CAST(@DateTime AS datetime2(1)); --2016-01-01 00:00:00.0 SELECT CAST(@DateTime AS datetime2(2)); --2016-01-01 00:00:00.03 SELECT CAST(@DateTime AS datetime2(3)); --2016-01-01 00:00:00.003 SELECT CAST(@DateTime AS datetime2(4)); --2016-01-01 00:00:00.0033 SELECT CAST(@DateTime AS datetime2(5)); --2016-01-01 00:00:00.00333 SELECT CAST(@DateTime AS datetime2(6)); --2016-01-01 00:00:00.003333 SELECT CAST(@DateTime AS datetime2(7)); --2016-01-01 00:00:00.0033333 GO DECLARE @DateTime datetime = '2016-01-01T00:00:00.007'; SELECT CAST(@DateTime AS datetime2(0)); --2016-01-01 00:00:00 SELECT CAST(@DateTime AS datetime2(1)); --2016-01-01 00:00:00.0 SELECT CAST(@DateTime AS datetime2(2)); --2016-01-01 00:00:00.01 SELECT CAST(@DateTime AS datetime2(3)); --2016-01-01 00:00:00.007 SELECT CAST(@DateTime AS datetime2(4)); --2016-01-01 00:00:00.0067 SELECT CAST(@DateTime AS datetime2(5)); --2016-01-01 00:00:00.00667 SELECT CAST(@DateTime AS datetime2(6)); --2016-01-01 00:00:00.006667 SELECT CAST(@DateTime AS datetime2(7)); --2016-01-01 00:00:00.0066667 GO |
| --- |

Essa alteração de comportamento fornece um valor convertido mais preciso, mas pode quebrar aplicativos que esperam que o valor convertido seja o mesmo que o valor de data e hora arredondado como era o caso do SQL Server 2016.

Esteja ciente do que a precisão de data / data cheia completa (em vez do valor arredondado) também é usada ao avaliar predicados envolvendo um tipo de data e hora. A precisão total de ambos os argumentos é usada, resultando no predicado de comparação de igualdade para avaliar falso em ambos os scripts abaixo. O maior do que o predicado é verdadeiro no primeiro script e o menor que o predicado é verdadeiro no segundo:

| --Este Script altera o nível de compatibilidade para as versão do SQL Server 2016 ALTER DATABASE database\_name SET COMPATIBILITY\_LEVEL = 130 --Este script imprime o predicado IGUAL não é verdadeiro DECLARE @DateTime datetime = '2016-01-01T00:00:00.003'; DECLARE @DateTime2 datetime2(7) = @DateTime; IF @DateTime = @DateTime2 PRINT 'A igualdade entre @DateTime e @DateTime2 é verdadeira' ELSE PRINT 'A igualdade entre @DateTime e @DateTime2 não é verdadeira'; IF @DateTime < @DateTime2 PRINT 'O @DateTime é menor que o @DateTime2' ELSE PRINT 'O @DateTime não é menor que o @DateTime2'; IF @DateTime > @DateTime2 PRINT 'O @DateTime é maior que o @DateTime2' ELSE PRINT 'O @DateTime não é maior que o @DateTime2'; GO --Este script imprime o predicado IGUAL não é verdadeiro DECLARE @DateTime datetime = '2016-01-01T00:00:00.007'; DECLARE @DateTime2 datetime2(7) = @DateTime; IF @DateTime = @DateTime2 PRINT 'A igualdade entre @DateTime e @DateTime2 é verdadeira' ELSE PRINT 'A igualdade entre @DateTime e @DateTime2 não é verdadeira'; IF @DateTime < @DateTime2 PRINT 'O @DateTime é menor que o @DateTime2' ELSE PRINT 'O @DateTime não é menor que o @DateTime2'; IF @DateTime > @DateTime2 PRINT 'O @DateTime é maior que o @DateTime2' ELSE PRINT 'O @DateTime não é maior que o @DateTime2'; GO |
| --- |

Para fornecer informações sobre por que as comparações resultam em maior e menor que, respectivamente, o script abaixo mostra o valor de nanossegundos dos tipos de dados comparados:

| --Este Script altera o nível de compatibilidade para as versão do SQL Server 2016 ALTER DATABASE database\_name SET COMPATIBILITY\_LEVEL = 130 DECLARE @DateTime datetime = '2016-01-01T00:00:00.003'; DECLARE @DateTime2 datetime2(7) = @DateTime; SELECT DATEPART(nanosecond, @DateTime); --3333333 SELECT DATEPART(nanosecond, @DateTime2); --3333300 GO DECLARE @DateTime datetime = '2016-01-01T00:00:00.007'; DECLARE @DateTime2 datetime2(7) = @DateTime; SELECT DATEPART(nanosecond, @DateTime); --6666666 SELECT DATEPART(nanosecond, @DateTime2); --6666700 GO |
| --- |

O tipo datetime2 é preciso apenas para 100 nanosegundos, enquanto o datetime inclui valores para o nanosegundo (e além) porque a precisão teórica dos valores decimais repetidos é ilimitada. A implicação é que um tipo de data e hora com um valor decimal repetido nunca será comparado igualmente com qualquer tipo temporal, exceto o datetime.

O comportamento de conversão e comparação de data e hora é controlado pelo nível de compatibilidade do banco de dados. Bancos de dados no nível SQL Server 2016 (130) usam o novo comportamento e o comportamento legado é usado com outros níveis.

**Segue abaixo o link da documentação oficial da Microsoft sobre a mudança no campo DATETIME:**

**<https://msdn.microsoft.com/pt-br/library/ms187819(v=sql.120).aspx>**

**\*Importante: Recomendamos que para todos novos desenvolvimentos seja utilizado o tipo de dados DATETIME2.**
