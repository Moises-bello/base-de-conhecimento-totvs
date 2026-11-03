---
article_id: 360050786733
category: MDT - EPI
content_hash: 9b3c66e2341b813d7fddbf9b5bf45a14d2c34b8d7c2f4e1dab4f434870fb1bd3
fetched_at: '2026-06-28T22:44:25.447712+00:00'
product: protheus
section_id: 360010945554
source: central-protheus
title: RH - Linha Protheus - MDT - Entrega de EPI com baixa no estoque
type: support-article
updated_at: '2024-11-05T11:23:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050786733-RH-Linha-Protheus-MDT-Entrega-de-EPI-com-baixa-no-estoque
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/20197492048791)** Tempo aproximado para leitura:**00:03:00min  
  
Dúvida**Como realizar a entrega de EPI com baixa no estoque, criando uma movimentação simples na tabela **(SD3)**Movimentações Internas? Baixa/devolução epi automática.  
  
**Ambiente**TOTVS RH (Linha Protheus) - Medicina e Segurança do Trabalho - Todas as versões  
  
**Solução**Para saber como configurar um produto com o tipo EPI e seus principais parâmetros consulte os seguinte artigos:  
1.[MP - MDT - Como cadastrar um produto com o tipo EPI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360048704353-MP-MDT-Como-cadastrar-um-produto-com-o-tipo-EPI)  
2.[MP - MDT - Quais são os principais parâmetros de EPI](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360049532813)Temos disponíveis um vídeo demonstrando o passo a passo. Além do vídeo existe a documentação de apoio que pode ser acessada através do link: [MDT EPI](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360010945554-MDT-EPI)  
  
How To | MP - SIGAMDT - Como Entregar EPI Com Baixa no Estoque   
  
  
  
Após a conferencia acima, deverá habilitar o parâmetro de integração entre o Medicina e Estoque sendo o parâmetro **MV\_NGMDTES = S** e  **MV\_NG2SA = N.**Para isto acesse o **configurador ( SIGACFG),** no seguinte caminho: Atualizações > Cadastro > Parâmetro.

**![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077086393)  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075968414)  
  
*Acesso o módulo 35* ( SIGAMDT),** no seguinte caminho: Atualizações > Cadastro Gerais > Produto (EPI)  
  
![mceclip2.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075969674)  
  
Aponte o tipo EP = EPI e o armazém padrão.  
  
![mceclip3.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077089153)  
 **Importante:**Caso o parâmetro de integração de estoque esteja habilitado **(MV\_NGMDTES)**, é necessário que haja uma inclusão na rotina Inicial (MATA220), informando o EPI, armazém e a quantidade. Caso não haja esse cadastro, o sistema dispara a mensagem abaixo informando que o campo Armazém é inválido:  
  
![mceclip4.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075970114)  
  
Portanto se faz necessário acesso o módulo 04 **( SIGAEST)**, no seguinte caminho: Atualizações > Saldos > Inicial.  
  
![mceclip5.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075970254)  
  
Realize o cadastro apontando o produto, armazém e quantidade inicial.  
  
![mceclip6.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075970294)  
  
Retorne ao módulo 35 ( SIGAMDT) e realize o vinculo do Fornecedor com o Epi cadastrado. Através da rotina: Atualizações > EPI > Fornecedor x EPI. Acione EPIs e realize o cadastro.  
  
![mceclip7.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077089873)  
  
![mceclip8.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077089993)  
  
Basta realizar a entrega do EPI ao Funcionário e observar a baixa no estoque.  
  
![mceclip9.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077090673)  
  
Ao confirma a entrega é emitido o relatório de entrega.  
  
![mceclip10.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360077091553)  
  
Ao consultar o saldo atual no estoque observe que abateu as 5 mascaras que entreguei ao funcionário.  
Para esta consulta acesse Módulo 04 em Atualizações > Saldos > Atual.  
  
![mceclip12.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075972274)

![mceclip11.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360075972194)  
  
**Saiba Mais**[Central de Artigos Medicina e Segurança do Trabalho](https://centraldeatendimento.totvs.com/hc/pt-br/sections/1500000904781-Medicina-e-Seguran%C3%A7a-do-Trabalho-SIGAMDT-)  
[Como configurar o uso da Biometria no SIGAMDT](https://centraldeatendimento.totvs.com/hc/pt-br/articles/11169895277207)  
[Assistente Virtual Carolina](https://centraldeatendimento.totvs.com/hc/pt-br/sections/9198712823575-Assistente-Virtual-Carolina)
