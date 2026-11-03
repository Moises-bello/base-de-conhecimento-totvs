---
article_id: 360023381192
category: Planejamento e Controle da Produção (SIGAPCP)
content_hash: 167b0c1814e5980f9ccc5fa2daf299c78260c97b21224fcff2cb6fad4fac9e7f
fetched_at: '2026-06-28T22:42:42.286181+00:00'
product: protheus
section_id: 360005696274
source: central-protheus
title: Manufatura - Linha Protheus - SIGAPCP - Erro type mismatch on compare  on EXPLESTR
type: support-article
updated_at: '2026-05-14T20:12:08Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360023381192-Manufatura-Linha-Protheus-SIGAPCP-Erro-type-mismatch-on-compare-on-EXPLESTR
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20850551418263)** Tempo aproximado para leitura:**00:01:00 min**  
  
**Ocorrência**  
Na rotina **MATA650 - Ordens de Produção**, após confirmar a tela de empenhos é gerado o erro: **type mismatch on compare on EXPLESTR**.  
  
**Ambiente**  
TOTVS Manufatura - TOTVS Manufatura (Linha Protheus) - Planejamento e Controle da Produção (SIGAPCP) - Versão 12   
  
**Causa**  
Esse incidente ocorre quando é aberta uma ordem de produção e o componente que está na estrutura não está cadastrado na tabela **SB1 - Descrição Genérica do Produto**, ou os campos **B1\_COD - Código do Produto, G1\_COMP - Código do Componente e G1\_COD - Código do Produto** não possuem o mesmo tamanho ou ainda, o componente está cadastrado na tabela **SB1**, mas com o compartilhamento incorreto.  
  
**Solução**  
Para solucionar essa ocorrência, realize os seguintes passos:  
  
1. Verificar no dicionário de dados e no banco de dados se os campos **B1\_COD**, **G1\_COD** e **G1\_COMP** possuem o mesmo tamanho;  
2. Caso algum desses campos esteja fora do padrão, ajustar para o tamanho padrão;  
3. No arquivo **error.log** deverá localizar a tabela **SG1 - Estrutura dos produtos** utilizando a busca com espaço e dois asteriscos;

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360021246192)

4. Verificar qual produto está sendo referenciado no campo **G1\_COD(C) - Produto**do *log*;  
5. Acessar a rotina de **MATA010 - Cadastro de Produto** e verificar se o componente está cadastrado na **SB1**.  
6. Caso o componente não está cadastrado é necessário realizar o ajuste, cadastrando esse componente no **MATA010** ou excluindo da **Estrutura - MATA200**.
