---
article_id: 1500000455722
category: ADVPL - Classe e Função
content_hash: 1f807fbbaf26274ce9b2626d2d2a29e0bcfea85c02fdab5baa7626361a18401a
fetched_at: '2026-06-28T22:40:14.587669+00:00'
product: protheus
section_id: 1500001538041
source: central-protheus
title: 'Cross Segmento - TOTVS Backoffice Linha Protheus - ADVPL - Classe FWPrintSetup:
  Método GetProperty() e suas propriedades'
type: support-article
updated_at: '2022-01-04T21:34:39Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500000455722-Cross-Segmento-TOTVS-Backoffice-Linha-Protheus-ADVPL-Classe-FWPrintSetup-M%C3%A9todo-GetProperty-e-suas-propriedades
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png)Tempo aproximado para leitura: **00:03:00 min  
  
Dúvida**Quais as ações da propriedade método GetProperty() na classe FwPrintSetup?

**Ambiente**Cross Segmento - TOTVS Backoffice (Linha Protheus) – ADVPL – A partir da versão 12.1.17

**Solução  
PD\_DESTINATION -> DESTINO DA IMPRESSÃO**  
recupera a informação do destino da impressão, local (*smartclient* *desktop*) ou servidor (*appserver*)  
1 - servidor  
2 - local

**PD\_PRINTTYPE -> TIPO DA IMPRESSÃO**  
recupera o tipo da impressão definida, esta informação pode variar conforme o componente utilizado  
na **fwmsprinter** as possibilidades são:  
1 - *spool*  
6 - pdf

**PD\_ORIENTATION -> ORIENTAÇÃO DA PÁGINA DURANTE A IMPRESSÃO**  
recupera a orientação definida para a página na impressão  
1 - retrato  
2 - paisagem

**PD\_PAPERSIZE -> TAMANHO DO PAPEL**  
recupera a informação da dimensão do papel utilizado na impressão, esta lista pode variar conforme o componente  
utilizado na impressão, na **fwmsprinter** as possibilidades são:  
1 - "Letter 8 1/2 x 11 in"  
2 - "A4 210 x 297 mm"  
3 - "A3 297 x 420 mm"  
4 - "Executive 7 1/4 x 10 1/2 in"  
5 - "Tabloid 11 x 17 in"

```
Tentar definir algo diferente da lista causa comportamentos inadequados durantes a impressão.
```

**PD\_PREVIEW -> EXIBE EM TELA?**  
recupera a configuração para exibir janela com a imagem da impressão antes de enviar para a impressora.  
Essa configuração tem valor do tipo lógico e o padrão dessa configuração é falso.  
Não é assegurado que o exibido na tela seja o resultado da impressão no papel.  
Os *drivers* e comunicação *appserver*, *printer.exe* com a impressora afetam o resultado no papel.

**PD\_VALUETYPE -> TIPO DE VALOR ("Imp\_Spool IMP\_PDF") //Define saída de impressão**  
recupera o nome do arquivo e endereço definido para a impressão ou geração.

**PD\_MARGINMARGEM -> MARGEM**  
recupera a definição das margens da página a serem respeitadas na impressão  
O retorno é uma lista com os valores definidos para:  
1 - margem esquerda  
2 - margem superior  
3 - margem direita  
4 - margem inferior

**Saiba mais**[FWPrintSetup](https://tdn.totvs.com/display/public/PROT/FWPrintSetup)
