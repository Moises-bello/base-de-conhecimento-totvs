---
article_id: 360060150674
category: Fiscal Arquivos Magnéticos - Extrator Fiscal
content_hash: 8fb98bf504bb70aa80de5666d1dbc6ace8c6fa6ca84fff0a31be9560453d62a4
fetched_at: '2026-06-28T22:42:07.750420+00:00'
product: protheus
section_id: 1500001535021
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Extrator Fiscal
  - Como Integrar o Layout T013
type: support-article
updated_at: '2022-08-18T17:23:32Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360060150674-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Extrator-Fiscal-Como-Integrar-o-Layout-T013
---

**Dúvida**

 Como Integrar o Layout T013?  
  
**Ambiente**  
Microsiga Protheus – Livros Fiscais – A partir da versão 12  
  
**Solução**

A nota precisa gerar livro fiscal  (SF3/SFT). No caso de Reinf, deve ser gerado livro de ISS, conforme exemplo abaixo:

TES

**Para calcular  e tributar o ISS :**

Calcula ISS(F4\_ISS) = Sim

L.Fiscal.ISS(F4\_LFISS) = Tributado

 

**Para calcular o ISS, e não tributar:**

Calcula ISS(F4\_ISS) = Não

L.Fiscal.ISS(F4\_LFISS) = Outros

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046778994/mceclip0.png)

ou

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046779074/mceclip1.png)

 

Para o caso de outros tipos de notas, qualquer pergunta referente a livro fiscal não pode estar como não, para que a nota gere SFT e SF3.

Caso a nota já tenha sido gerada, após a alteração, entre na rotina MATA930 e reprocesse o livro fiscal. Caso surgir alguma dúvida no processo de escrituração da nota e rotina de reprocessamento, acionar o suporte do Time Protheus Fiscal da TOTVS.

Caso se tratar de Reinf, o Código de serviço deve estar vinculado na rotina mata963, conforme o link abaixo. 

<https://tdn.totvs.com/pages/releaseview.action?pageId=354473827>

 

Consulte o parâmetro MV\_INTTAF , ele foi descontinuado e precisa estar como N.

Consulte o parâmetro MV\_TAFLPRC, precisa estar com o conteúdo padrão 2000.

O extrator fiscal não valida a data de emissão, para levar o documento para o TAF é validado a data de entrada do documento, então se a emissão foi no dia 31/01/2019, mas a nota só entrou no sistema no dia 03/02/2019, além de extrair o mês de Janeiro você deve executar o mês de Fevereiro para que a nota seja levada para o TAF.

Para evitar que ocorra erros de integração, é importante que ao selecionar o Layout T013, seja selecionado os layouts de Cadastros também. A configuração recomendada de extração para Reinf segue abaixo:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360046780094/mceclip2.png)

 

Efetue o processamento no modulo 84.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027345912/mceclip0.png)

 

Vá em, Miscelânea, Integração, Processamentos

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027351211/mceclip2.png)

 

Configure o processamento conforme abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027351371/mceclip3.png)

Após o processamento, Valide o gerenciador de integração, caso exista alguma inconsistência na integração.

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027346492/mceclip4.png)

 

Deve ser selecionado o dia do processamento.

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027352011/mceclip5.png)

 

Na tela a seguir é gerado um ticket, caso ocorra algum erro de integração é gerado com a legenda vermelha.

 

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360041399393/mceclip1.png)

Caso a integração ocorra sem erros, é gerado conforme imagens abaixo:

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027347092/mceclip6.png)

 

 

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360027347292/mceclip8.png)

Caso após as orientações acima o Layout T013 não ser importado pelo Extrator Fiscal, realize a abertura de um chamado com a Equipe TOTVS.
