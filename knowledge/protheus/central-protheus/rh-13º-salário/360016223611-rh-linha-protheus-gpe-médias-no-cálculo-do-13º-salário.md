---
article_id: 360016223611
category: RH - 13º salário
content_hash: 2bf408a8fa830a66a8cd486d72f3448c451e18e5287a81a05a22bb6d8d07e689
fetched_at: '2026-06-28T22:44:00.853919+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Médias no cálculo do 13º Salário
type: support-article
updated_at: '2025-08-15T18:53:17Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016223611-RH-Linha-Protheus-GPE-M%C3%A9dias-no-c%C3%A1lculo-do-13%C2%BA-Sal%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/19058745713047) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Como realizar a parametrização de médias no cálculo do 13º Salário?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução**São 3 configurações a serem feitas para o cálculo de média: Cadastro de verbas, Cadastro de Sindicatos e o mnemônico P\_MEDDIREN.

- **Cadastro de Verbas**

![](https://totvssuporte.zendesk.com/attachments/token/bxrVZjeMM8LpRjNlvHCknU5m0/?name=inline-628229754.png)

O cadastro de verbas deve ser configurado com **S** ou **N**.

Com **S** o sistema considera a verba como média e olha as configurações do cadastro de sindicatos;  
Com **N** a verba não é considerada como média;  
 **Observação:** Deve possuir os seguintes **identificadores de cálculo** vinculados a uma verba:

- ID de cálculo **1628** - Total de Medias em Valor 1ª Parc;

- ID de cálculo **1629** - Total de Medias em Horas 1ª Parc;

- ID de cálculo **0123** - Total de Médias em Valor;

- ID de cálculo **0124** - Total de médias em Horas.

- **Cadastro de Sindicatos**

![](https://totvssuporte.zendesk.com/attachments/token/i12XehIcf6MiTwZ2JnAmfUVLk/?name=inline828708726.png)​

Quando os campos **Meses média 1º** (Que nesse caso é o primeiro período de apuração), **Meses média 2º,**etc... estão preenchidos com 3 / 6 / 12, por exemplo, e as verbas que entram para média (Hora Extra por exemplo) está com **S** (de Sindicato) o sistema verifica no período (Ano do cálculo do 13º), busca as médias e avalia as 3 maiores / 3, as 6 maiores / 6, as 12 médias do período e /12, as que derem resultado mais favorável para o funcionário, o sistema irá utilizar.

**Exemplo**:

3 últimos meses – 1.200,00 (Total de médias) / 03 = 400,00

6 últimos meses – 4.000,00 (Total de médias) / 06 = 750,00

12 últimos meses – 4.500,00 (Total de médias) / 12 = 375,00  
  
Deixando os campos **zerados**o sistema buscará as médias de todo período e a divisão será por 12.

**- Mnemônico P\_MEDDIREN**

​​![](https://centraldeatendimento.totvs.com/hc/article_attachments/13263118896279)

O mesmo deve ser preenchido com **S,** **N ou M.** Este parâmetro define como será a divisão das médias.  
  
Quando configurado com **S -** para que a soma das verbas com incidência para médias seja dividida pela quantidade de meses de direito. **Calculo:** Total das médias / 12 \* Avos de direito = Valor média Pagamento.  
  
Quando configurado com **N -** para que a soma das verbas com incidência para médias seja dividida por 12 e em seguida multiplicado pelos meses de direito. **Calculo:** Total Médias / Avos de Direito = Média. Após o primeiro cálculo faz-se : Média / 12 \* Avos de Direito = Valor Média Pagamento.  
  
Quando configurado com **M**- Misto, para que o mnemônico seja alterado em tempo de execução de acordo com o tipo de contrato do funcionário, conforme [orientação da consultoria de segmentos](https://tdn.totvs.com.br/pages/releaseview.action?pageId=134152319), sendo:  
- Se o tipo de contrato for por tempo indeterminado ou for por tempo determinado e contrato superior a 12 meses, o mnemônico é utilizado como "N".  
- Se o tipo de contrato for por tempo determinado e o contrato igual ou inferior a 12 meses, o mnemônico é utilizado como "S".  
  
**Configuração 1****P\_MEDDIREN = M - Neste caso cálculo é efetuado como se o parâmetro fosse preenchido com "S"**  
Funcionário com contrato por tempo determinado e duração igual ou inferior a um ano.

**Cálculo:**  
Total das médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Valor média PAGAMENTO.

**Configuração 2**  
**P\_MEDDIREN = M -** Neste caso o cálculo é efetuado como se o parâmetro fosse preenchido com "N"  
Funcionário com contrato por tempo determinado e duração superior a um ano.

**Calculo:**  
Total Médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Média  
Média / 12 \* Avos de Direito = Valor Média Pagamento

**Configuração 3**  
**P\_MEDDIREN = M -** Neste caso o cálculo é efetuado como se o parâmetro fosse preenchido com "N"  
Funcionário com contrato por tempo indeterminado.

**Calculo:**  
Total Médias (Somatório das verbas com incidência para média) / Meses considerados para média\* = Média  
Média / 12 \* Avos de Direito = Valor Média Pagamento.

**Importante**  
Não confundir o funcionamento do mnemônico P\_MEDDIREN (Parâmetro MV\_MEDDIRE) com a quantidade de meses para médias no cadastro de sindicatos ou no cadastro de verbas. Os meses definidos nesses cadastros são utilizados para obter o somatório total de verbas para base das médias e mais informações podem ser obtidas [neste documento](https://tdn.totvs.com/pages/viewpage.action?pageId=724597392).   
O mnemônico P\_MEDDIREN define se esse somatório será dividido pelos dias de direito ("S") ou se será dividido por 12 e multiplicado pelos meses considerados para média ("N").

**Reforçando**  
Quando o parâmetro é preenchido com "M", o cálculo é efetuado pelos dias de direito somente para funcionários com contrato por tempo determinado e duração igual ou inferior a um ano. Para todos os demais casos o cálculo é efetuado como se o parâmetro fosse preenchido com "N".  
Mais informações sobre o preenchimento com "M" pode ser obtido [aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=721741236).

**Saiba Mais**[Artigos 13° Salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio?page=3#articles)[Como analisar as médias no cálculo de 13º Salário](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360015780592)  
[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)  
Essas **documentações** também podem ser acessadas através da **Carolina**, veja como acessar a assistente virtual, via **Protheus** ou central de atendimento: <https://www.youtube.com/watch?v=T7b4zMlphTI>
