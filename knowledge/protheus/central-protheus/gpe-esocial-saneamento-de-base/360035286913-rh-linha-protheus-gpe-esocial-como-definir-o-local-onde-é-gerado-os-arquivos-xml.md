---
article_id: 360035286913
category: GPE - eSocial - Saneamento de Base
content_hash: 03bf44b9a5754cb8768fd45c32646874a41baa94c5237bae4e8c79548af0adf3
fetched_at: '2026-06-28T22:45:01.593655+00:00'
product: protheus
section_id: 360007319754
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - Como definir o local onde é gerado os
  arquivos XML's de eventos eSocial quando utilizado o parâmetro MV_XMLGPE
type: support-article
updated_at: '2024-12-04T14:56:20Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035286913-RH-Linha-Protheus-GPE-eSocial-Como-definir-o-local-onde-%C3%A9-gerado-os-arquivos-XML-s-de-eventos-eSocial-quando-utilizado-o-par%C3%A2metro-MV-XMLGPE
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18026641370647) Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Como definir o local onde é gerado os arquivos **XML's** de eventos **eSocial** quando utilizado o parâmetro **MV\_XMLGPE?**  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Solução** **1.** Para gerar o arquivo XML do SIGAGPE o parâmetro **MV\_XMLGPE** deverá estar habilitado. Para ativá-lo, acesse a rotina **Parâmetros** no **Configurador**, busque pelo **MV\_XMLGPE**  e altere o conteúdo do parâmetro para **.T.**Caminho: SIGACFG > Ambiente > Cadastros > Parâmetros:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18026201359639)  
![2021-04-13_11-38-51.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009156802)  
  
**2.** Para alterar o local de gravação do arquivo XML, será necessário acessar a rotina de **Carga Inicial** no **SIGAGPE**. Clicar em **Outras Ações** e selecionar a opção **Parâmetros grav. XML**, definir o caminho onde será gravado, salvar e sair da rotina.  
Caminho: SIGAGPE > Miscelânea > eSocial > Carga Inicial:  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/18026453783447)  
![2021-04-13_11-41-21.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/1500009155802)  
  
**Observação**

* Não é necessário manter o parâmetro **habilitado**. Só é recomendável habilitar em casos de erro onde é necessário analisar o XML antes da integração com o TAF.
* Os arquivos gerados com o parâmetro habilitado são apenas para análise então não é necessário mantê-los gravados;
* Caso o caminho na opção **parâmetros grav. XML** esteja em branco o sistema vai gravar na pasta system os registros.
* Para outras formas de gerar XML consulte o artigo: [**Como gerar o XML de eventos eSocial integrados do SIGAGPE com o SIGATAF para analise do suporte técnico**](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360006744012).

**Saiba Mais**Para saber mais consulte os *links* abaixo:   
[eSocial | Protheus - Entregas Legais](https://tdn.totvs.com/display/public/PROT/eSocial+%7C+Protheus+-+Entregas+Legais)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
  
Essa documentação também pode ser acessada 24h, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
