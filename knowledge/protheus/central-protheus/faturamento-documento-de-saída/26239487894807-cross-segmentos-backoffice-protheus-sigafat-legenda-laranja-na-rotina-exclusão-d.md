---
article_id: 26239487894807
category: FATURAMENTO - DOCUMENTO DE SAÍDA
content_hash: 24b250e2de8078df3b917a428488361695ff3c78ca4581521e958e2618967cc3
fetched_at: '2026-06-28T22:38:44.075125+00:00'
product: protheus
section_id: 1500001539161
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - SIGAFAT - Legenda laranja na rotina
  Exclusão Documento de Saida
type: support-article
updated_at: '2026-04-01T20:28:58Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/26239487894807-Cross-Segmentos-Backoffice-Protheus-SIGAFAT-Legenda-laranja-na-rotina-Exclus%C3%A3o-Documento-de-Saida
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26239495729687) Tempo aproximado para leitura: **00:05:00 min**

**Ocorrência**  
Ao tentar excluir documento de saída foi retornado a legenda laranja e não exclui.  
  
**Ambiente**  
Cross Segmentos - Backoffice Protheus - SIGAFAT – Todas as versões  
  
**Causa**  
A legenda laranja significa "Aguardando Cancelamento", ou seja, um problema de comunicação com SEFAZ ou SPED Protheus, pois o job só exclui ou dá retorno se obter validação pelo SEFAZ  
  
**Solução**

**1 - Tenha em mãos a chave NFE (campo "Chave (F2\_CHNVFE)")**

Valide na SEFAZ para ver se está na SEFAZ HOMOLOGAÇÃO ou SEFAZ PRODUÇÃO. A mesma chave só pode estar em um ambiente SEFAZ

Coloque a chave XML (campo F2\_CHVNFE do cabeçalho da nota fiscal de saída) na Homologação Sefaz e consulte para ver se aparece:  
<https://hom.nfe.fazenda.gov.br/portal/principal.aspx>   
  
Coloque a chave XML (campo F2\_CHVNFE do cabeçalho da nota fiscal de saída) na Produção Sefaz e consulte para ver se aparece:  
<https://www.nfe.fazenda.gov.br/portal/principal.aspx>

Em qual ambiente retornar, é o ambiente em que a nota fiscal de saída foi transmitida.

**2 - Vá na rotina "NFESEFAZ > Outras Ações > NFe"**

Verifique se o pergunte "**Ambiente ?**" está configurado igual onde está transmitido a nota.

Se a nota foi transmitida em homologação tem de estar "**2-Homologacao**", se foi transmitida em produção o pergunte tem de estar "**1-Producao**":

![](https://centraldeatendimento.totvs.com/hc/article_attachments/32289251619735)

**3 - Se for NFe, consulte no site do órgão** [**SEFAZ (https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx)**](https://www.nfe.fazenda.gov.br/portal/disponibilidade.aspx) **do estado do cliente, se for NFs, consulte o site da prefeitura do estado do cliente.**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/32289251622935)**

Veja se os serviços para o estado do cliente da nota fiscal de saída estão ativos.

Caso não estejam, será necessário aguardar o restabelecimento dos serviços para tentar processar a exclusão novamente.

**Observação:** Interrupções nos serviços da Sefaz ou da Prefeitura não são de responsabilidade da TOTVS, sendo necessário entrar em contato diretamente com o órgão responsável.

**4 -** **Reavalie a configuração do** **FATJOBNFE, veja se ele foi configurado o JOB e HORÁRIOS em chaves no "appserver.ini" ou pelo "Schedule" do configurador (SIGACFG)**

A - Se está configurado nas chaves do appserver.ini e ***só tem uma filial*** usando o FATJOBNFE:

![FATJOB_FILIAL_UNICA.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32289251624599)

B - Se está configurado nas chaves do appserver.ini e tem ***mais de uma filial*** usando o FATJOBNFE:

![FATJOB_VARIAS_FILIAIS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32289262547479)

C - Se está configurado corretamente o "Schedule do configurador":

![schedule.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32289251633431)

**OBS 1:** Faça isso para cada filial (caso esteja usando o FATJOBNFE em mais de uma)

**OBS 2:** Importante ressaltar que a configuração do Schedule tem o consumo de licenças. 

O JOB precisa estar configurado corretamente, consulte aba Configuração: [Job para exclusão documento de saída (MATA521) - FATJOBNFE](https://tdn.totvs.com/x/tr44E)

**5 - Verifique se o serviço do Protheus TSS X Sefaz está ativo, para isto acesse a rotina "NFESEFAZ".**

Caso apresente a mensagem abaixo significa que o TSS está com o serviço parado, é necessário habilitar e processar a exclusão novamente:

![image (1).png](https://centraldeatendimento.totvs.com/hc/article_attachments/26239495732375)

**OBS:** Não conseguindo resolver o erro do tópico acima (5), contate a Equipe Protheus SPED

**6 - Parâmetros MV\_CANCNFE (para notas de venda) e MV\_CANNFSE (para notas de serviço)**

![PARAMETROS.png](https://centraldeatendimento.totvs.com/hc/article_attachments/32289251635479)

Caso esses parâmetros estejam com filial em branco, **TODAS** as filiais da empresa tem de ter a configuração do FATJOB.

Se a filial estiver preenchida, só basta realizar a configuração do FATJOBNFE para aquela filial (no appserver.ini ou schedule)

**OBS:** Pode ser que esteja preenchido uma filial que não possuam intenção de ter o FATJOBNFE e terem de retirar, ou, caso não usem o FATJOBNFE em todas as filiais, criar o parâmetro por filial só nas filiais que utilizam.

**7 - Atualize a requisição no documento de saída.**  
Vá na rotina "MATA521A - Exclusão dos documentos de saída" > Outras ações > "Atualizar"

**OBS:** Caso fique diferente de laranja após o procedimento acima, contate a Equipe Protehus SPED para demais informações!

**8 - O erro permaneceu?**

Caso o erro permaneça, envie ao suporte:

* Print de todos os tópicos (1, 2, 3, 4, 5 e 6):
* Conteúdo do campo "Flag de Impressao (F2\_FIMP)" da nota com legenda laranja
* Conteúdo do campo "Status (F2\_STATUS)" da nota com legenda laranja
