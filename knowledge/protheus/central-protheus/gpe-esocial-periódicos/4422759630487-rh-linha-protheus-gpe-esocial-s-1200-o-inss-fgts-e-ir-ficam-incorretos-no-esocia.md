---
article_id: 4422759630487
category: GPE - eSocial - Periódicos
content_hash: cbb2d8e7744534f1f3e32b5dc9a7776bc82f413400f02f0b19d96e3b188e475d
fetched_at: '2026-06-28T22:45:08.683265+00:00'
product: protheus
section_id: 360005445793
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-1200 - O INSS, FGTS e IR ficam incorretos
  no eSocial (DCTFWEB) quando existe Férias no mês
type: support-article
updated_at: '2025-09-04T18:57:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4422759630487-RH-Linha-Protheus-GPE-eSocial-S-1200-O-INSS-FGTS-e-IR-ficam-incorretos-no-eSocial-DCTFWEB-quando-existe-F%C3%A9rias-no-m%C3%AAs
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/15193253552023) Tempo aproximado para leitura: 00:05:00 min****Ocorrência**As bases de INSS, FTGS e IR ficam incorretas no eSocial (DCTFWEB) quando existe Férias no mês.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Causa**  
Como no *layout* simplificado as informações dos valores de Férias são geradas no S-1200 em recibo separado, e também é gerado novamente no recibo de folha, isso faz com que a base de INSS e FGTS fique de forma incorreta ou duplicado no governo.  
  
**Solução**No *layout* simplificado o sistema envia os valores do calculo no recibo de Férias no período em que foi pago e os mesmos valores também são enviados no recibo da Folha no período de gozo, isso está correto, essas informações são esperadas pelo governo. Com isso para que não ocorra duplicidade na base de calculo INSS, FGTS e IR é necessário que exista no ambiente as verbas com os ID p/cálculo **1870, 1871, 1872, 1882 e 1893****.**Sugestão de preenchimento das configurações das verbas/rubricas:

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| **Id Verba** | **Tipo da Verba** | **Natureza** | **Cd. Inc. CP** | **Cd. Inc. FGTS** | **Cd.Inc. IRRF** | **Incidência Folha** |
| 1870 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 11 | 00 | Sem Tributação\* | Não |
| 1871 | 3 - Base Provento (Informativa) | 9989 | 31 | 00 | Sem Tributação\* | Não |
| 1872 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 00 | 11 | Sem Tributação\* | Não |
| 1882 | 4 - Base Desconto (Informativa Dedutora) | 9989 | 00 | 12 | Sem Tributação\* | Não |
| 1893 | 3 - Base Provento (Informativa) | 9989 | 00 | 00 | 33 | Não |

\* Os identificadores não terão tributação de IRRF, a escolha do código de incidência a ser utilizado nesse preenchimento é de responsabilidade da empresa.   
  
**Exemplo de Caso:**  
No meu exemplo a verba **C70** está vinculado ao ID 1870, a **A98** vinculado ao ID 1871 e **C72** vinculado ao ID 1872   
  
**1. Calculo de****Férias**  
As verbas destacadas na imagem abaixo são as verbas com tributação de **INSS** e **FGTS**, sendo nesse exemplo, férias e 1/3 férias  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7542194869143)  
  
Abaixo demostro as verbas que representam o desconto de INSS

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8758044809367)  
  
O valor da verba **A98** representa a verba de contrapartida do desconto de INSS  Por se tratar de verba de BASE elas não vai interferir no liquido, mas é fundamental para o cálculo de base do governo não ocorrer em duplicidade.  
**Observação: As verbas com os identificadores destacados na imagem abaixo deverão obrigatoriamente existir no cálculo de férias.**  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/8758081142295)

* Essas informações podem ser visualizadas no SIGAGPE (07) no caminho: **Miscelânea > Cálculos > Férias**.
* O ID **1882** aparece somente quando existe adiantamento do 13º no cálculo das férias.

**2. Calculo da Folha**  
No calculo da folha as verbas com os ID's **1870, 1871 e 1872** não são geradas. Essas verbas são apresentadas apenas no calculo das férias.  
Somente o identificador **1893** será apresentado na folha de pagamento, ele não será gerado no calculo de férias.  
  
**3. Relatório S-1200**  
Na imagem abaixo está sendo apresentado um exemplo do relatório S-1200 onde informei os totais apenas para ilustrar que existe o recibo de Folha e Férias, porem como existe as verbas de dedução das base de INSS e FGTS no recibo de Férias, a base não vai ficar duplicada no governo.   
  
Para saber como gerar esse relatório consulte: **[Como gerar relatório de conferência do evento S-1200 no GPE antes de integrar o evento periódico para o TAF](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360033101334).**  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/7544489192599)  
 **4. Evento S-1200 no TAF**  
A imagem abaixo foi apenas para ilustrar que no S-1200 existe as informações de recibo de Folha e Férias (que será integrado no período de apuração em que as férias foram pagas, devido a necessidade de totalizar o valor de IRRF pago nas férias, podendo ser no mesmo período de gozo ou anterior). O **S-1200** pode ser acessado no TAF (84) através do caminho: **A****tualizações > Eventos eSocial > Periódicos > Folha de Pagamento** (TAFA250).  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4422741899927)

**Atenção**

Com as verbas cadastradas corretamente, as verbas com incidência INSS e FGTS devem apresentar no cálculo FER, e a de IRRF no cálculo FOL. Caso não esteja deve ser executado o UPDBINFER, conforme apresentado na documentação: [RH - Linha Protheus - GPE - Rotina GPEM026I (Antigo Rdmake UPDBINFER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER).  
  
Para os casos onde o valor de INSS ou FGTS está incorreto no governo é necessário que reavalie todos os tópicos anteriores, e com atenção especial a incidências de cada verbas, pois muitos casos está relacionado a tributação incorreta. Também é necessário que consulte no site do governo a incidência da verba (rubrica) afim de verificar se a alteração compete ao período de apuração que está sendo realizado:  
[S-1010 - Como consultar no site do eSocial dados do evento S-1010 (Tabelas de Rubricas).](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360043153534)  
  
Caso seja necessário fazer algum ajuste de incidência, ou verbas, será necessário enviar o S-1200 novamente ao governo para reprocessar as informações da base de calculo. Consulte: [Como retificar ou reprocessar os Totalizados (DCTFWEB) no eSocial.](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025678254)

**Importante:**

* Para os casos onde já existe verbas com os IDs **1870, 1871, 1872 e 1882** (quando houver 13º salário) no cálculo das férias, não é necessário executar a [Rotina GPEM026I (Antigo Rdmake UPDBINFER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER).
* Para os casos no qual os valores de férias já estavam calculados antes de cadastrar as verbas com os ID's, existe a [Rotina GPEM026I (Antigo Rdmake UPDBINFER)](https://centraldeatendimento.totvs.com/hc/pt-br/articles/29282097999511-RH-Linha-Protheus-GPE-Rotina-GPEM026I-Antigo-Rdmake-UPDBINFER) que gera os ID's dentro do calculo já realizado. A Rotina GPEM026I deve ser executado apenas após a integração do roteiro **FER**, portanto a rotina não deve ser executada caso este roteiro ainda esteja aberto.

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[S-1200 - Diferença no INSS quando existe Férias no mês e verba com incidência de suspensão 91 ou 95](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6778582967063)  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
[Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602)

Quer receber em primeira mão sobre artigos publicados? Participe da nossa [**Comunidade WhatsApp**](https://chat.whatsapp.com/DJCIHJOMrC65a262mwAIEI?utm_source=whatsapp&utm_medium=-&utm_campaign=backoffice&utm_term=gsp&utm_content=-)📲

*Para conhecimento dos eventos futuros, acessa a nossa página **[TOTVS Informa](https://informa.totvs.com/)**selecione em categorias a área e pesquise por "**Eventos**".*
