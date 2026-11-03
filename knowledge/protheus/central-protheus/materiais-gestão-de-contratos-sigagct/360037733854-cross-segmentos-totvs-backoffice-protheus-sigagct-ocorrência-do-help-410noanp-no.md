---
article_id: 360037733854
category: Materiais - Gestão de Contratos - (SIGAGCT)
content_hash: cc586ce7bf7821404a83c3789b6df35b0d195152e76d190af7963d214846c84e
fetched_at: '2026-06-28T22:37:20.089363+00:00'
product: protheus
section_id: 1500001539581
source: central-protheus
title: 'Cross Segmentos - Totvs Backoffice Protheus - SIGAGCT - Ocorrência do Help:
  410NOANP - No Encerramento da Medição'
type: support-article
updated_at: '2022-05-19T20:51:28Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360037733854-Cross-Segmentos-Totvs-Backoffice-Protheus-SIGAGCT-Ocorr%C3%AAncia-do-Help-410NOANP-No-Encerramento-da-Medi%C3%A7%C3%A3o
---

**Dúvida**

Ocorrência do Help: 410NOANP - No Encerramento da Medição

**Ambiente**

Protheus – Compras – A partir da versão 12.1.17  
  
**Solução**

Ao realizar o encerramento de uma medição está ocorrendo o erro abaixo:

AJUDA: **410NOANP**  
Campo obrigatório não preenchido no cabeçalho.

![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049517314/mceclip0.png)

Esta mensagem está relacionada ao campo "**Modal ANP**" (**C5\_MODANP**) do cabeçalho do Pedido de Vendas, no qual o sistema está exigindo o seu preenchimento.

- Primeiramente deve-se verificar se este campo está como "obrigatório" no Dicionário de Dados.

**Obs**: Na formatação padrão do sistema este campos ele não é obrigatório e então deve retirar esta obrigatoriedade caso ele não necessite ser preenchido:

![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049518474/mceclip4.png)

- Se o campo não estiver como "Obrigatório" no Configurador, deve-se verificar se o parâmetro **MV\_DCLNEW** está habilitado e, caso esteja, realizar o teste desabilitando-o, verificando se a mensagem deixa de ocorrer:

![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360050408473/mceclip2.png)

![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049518194/mceclip3.png)

Se ao desabilitar o parâmetro, não apresentar o Help, existem duas opções:

- Deixar o parâmetro desabilitado ou caso haja a necessidade deste parâmetro **MV\_DCLNEW** estar ativo devido ao processo em questão, deve-se inserir um Inicializador Padrão no cadastro do campo **C5\_MODANP** com uma das opções de preenchimento existentes para o campo no cadastro de Pedido de Vendas.

![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049518094/mceclip1.png)

Opções no Pedido de Vendas:

![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360049519314/mceclip5.png)

Caso necessário incluir o inicializador padrão no campo acima, deve ser avaliado em conjunto com departamento de TI da empresa para atender o processo de acordo com a empresa.

**Saiba Mais:**

[SIGAGCT - Gestão de Contratos](https://tdn.totvs.com/pages/releaseview.action?pageId=223150221)

[MP - SIGAGCT - Natureza no encerramento da medição de Contrato Vendas - MV\_1DUPTNAT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024543871-MP-SIGAGCT-Natureza-no-encerramento-da-medi%C3%A7%C3%A3o-de-Contrato-Vendas-MV-1DUPTNAT)

[MP - SIGAGCT - Pontos de entrada para rotinas de Medição](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022685112-MP-SIGAGCT-Pontos-de-entrada-para-rotinas-de-Medi%C3%A7%C3%A3o)

[Artigos Materiais - Gestão de Contratos - (SIGAGCT)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/115001302787-Materiais-Gest%C3%A3o-de-Contratos-SIGAGCT-)
