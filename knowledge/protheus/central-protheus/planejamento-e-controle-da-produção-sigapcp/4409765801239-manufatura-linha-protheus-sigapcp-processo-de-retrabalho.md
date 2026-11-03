---
article_id: 4409765801239
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: a44414e785981217d24c965dd05d629533bdb74aa326481dd03e2bb1b6770de4
fetched_at: '2026-06-28T22:42:45.751211+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Processo de Retrabalho
type: support-article
updated_at: '2023-12-08T20:14:35Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/4409765801239-Manufatura-Linha-Protheus-SIGAPCP-Processo-de-Retrabalho
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360023589592/time.png) Tempo aproximado para leitura: **00:02:00 min** **Dúvida**Como realizar o processo de retrabalho de produtos para apresentação do **Bloco K260**?   
  
**Ambiente**TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Solução**Vamos utilizar uma estrutura simples e iremos retrabalhar o produto pai, o produto **PRODUTO\_PAI** já foi produzido em ordens de produções anteriores e encontra-se disponível em estoque.

![estrutura_retrabalho.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409761738263/estrutura_retrabalho.png)

1. O primeiro passo para realizar o retrabalho é cadastrar um novo produto na rotina **MATA010 – Produtos**, neste exemplo iremos utilizar o **PRODUTO\_RETRAB**, e para criar o vínculo deste produto com o produto acabado na seção **Complemento Produto PCP** no campo **VK\_PRDORI - Prod. Orig**. informe o código do produto a ser retrabalhado neste caso **PRODUTO\_PA**.

**![cadastro_produto_retrabalho.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409761754391/cadastro_produto_retrabalho.png)**

2. Segundo passo é transferir o saldo utilizando a rotina **MATA261 - Transferência Mod. II**, neste exemplo iremos transferir 100 unidades do produto **PRODUTO\_PA** para o **PRODUTO\_RETRAB**.  
  
3. Terceiro passo é abrir a **OP - Ordem de produção** para o produto **PRODUTO\_PA** e no campo **C2\_TPPR - Tp. Produção** informar o tipo **R - Retrabalho**. Ao confirmar os empenhos adicione o produto retrabalho, neste caso **PRODUTO\_RETRAB**, e também poderá excluir o componentes que não serão necessários no processo de retrabalho do seu produto.

![empenho_retrabalho.png](https://centraldeatendimento.totvs.com/hc/article_attachments/4409761786647/empenho_retrabalho.png)

Agora está tudo pronto, e é possível apontar a **OP** normalmente, o **Sped Fiscal** fará automaticamente a substituição dos códigos dos produtos, informando corretamente a receita a movimentação feita no registro **K260 - Reprocessamento e Reparo de Produto.**  
  
**Saiba mais**Para verificar a parametrização necessária para realizar o processo de retrabalho acesse: [Manufatura - Linha Protheus - SIGAPCP - Configuração de campos de retrabalho para Bloco K](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360053511473)  
Documentação completa do processo de retrabalho acesse o *link*: [Registro K260: Reprocessamento/Reparo de Produto/Insumo](https://tdn.totvs.com/x/r5N4Dw)  
Vídeo *How To* do processo de retrabalho acesse o *link*: [How To | Bloco K - OP de retrabalho](https://www.youtube.com/watch?v=5emQjhRPBv4)
