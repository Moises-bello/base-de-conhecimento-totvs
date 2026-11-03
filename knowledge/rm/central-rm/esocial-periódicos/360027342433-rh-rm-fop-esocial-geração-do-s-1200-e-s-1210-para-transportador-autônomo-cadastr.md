---
article_id: 360027342433
category: esocial - Periódicos
content_hash: 005d33a00c236fcf571c8e9c49f382aa7bb4ce37bfd9b2186c298a73ed81ef8f
fetched_at: '2026-06-28T22:47:09.405102+00:00'
product: rm
section_id: 1500000860982
source: central-rm
title: RH - RM - FOP - eSocial - Geração do S-1200 e S-1210 para transportador autônomo
  cadastrado no TOTVS Gestão Financeira
type: support-article
updated_at: '2024-06-28T12:29:21Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360027342433-RH-RM-FOP-eSocial-Gera%C3%A7%C3%A3o-do-S-1200-e-S-1210-para-transportador-aut%C3%B4nomo-cadastrado-no-TOTVS-Gest%C3%A3o-Financeira
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/24443230243991)** **Tempo aproximado para leitura: 00:02:30 min** **Dúvida**Como realizar a geração dos eventos S-1200 e S-1210 para transportados autônomo cadastrado no TOTVS Gestão Financeira?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha RM) - TOTVS Folha de Pagamento - eSocial - Todas as versões  
  
**Solução**Conforme MOS

![](https://centraldeatendimento.totvs.com/hc/article_attachments/24499907069335)

Desta forma, siga os passos abaixo para realizar a correta geração dos eventos S-1200 e S-1210 no RM:  
1. No TOTVS Gestão Financeira, preencha o cadastro do cliente/fornecedor focando nas abas Identificação, Tributos e eSocial;  
2. No lançamento financeiro:  
2.1. Informe o valor total da remuneração em **Valores | Gerais** campo **Valor Original**;  
2.2. Em **Valores | Tributos**, selecione **Entrar em Exibir Dados para Cálculo do INSS** na área **Valor do INSS**;  
2.2.1. Informe o **INSS do Empregado** no campo **Base (%)**;  
2.2.2. Clique no ícone do raio para o sistema calcular o valor de desconto do INSS com base no percentual indicado;  
2.3. Ainda em **Valores | Tributos**, selecione **Entrar em Exibir Dados para Cálculo do IRRF** na área **Valor do IRRF**;  
2.3.1. Informe no campo Base (%) o percentual relacionado ao IRRF do empregado;  
2.3.2. Clique no ícone do raio para o sistema calcular o valor de desconto do IRRF com base no percentual indicado;  
3. No TOTVS Folha de Pagamento, preencha as informações constantes no menu **Configurações | Parametrizador | eSocial | Autônomos Externos 1/2**;  
4. Preencha também as informações do menu **Configurações | Parametrizador | eSocial | Autônomos Externos 2/2**;  
5. Após esses procedimentos, acesse **eSocial | Gerar XML (Eventos Periódicos)** e gere os eventos S-1200 e S-1210 selecionando o campo **Gerar Autônomos do Fluxus/Externos**.  
  
**Importante**  
O lançamento financeiro do cliente fornecedor deve estar baixado para que a geração do S-1210 - Pagamentos de Rendimentos do Trabalho considere o lançamento.  
Acesse a página [Eventos S-1200 e S-1210 - Transportador autônomo - Autônomos cadastrados no Financeiro](http://tdn.totvs.com/pages/releaseview.action?pageId=463820907) para verificar no detalhe os campos e códigos de cálculo necessários para preenchimento dos cadastros.

**Saiba mais**  
Para mais informações acesse:   
- [Como gerar os eventos S-1200 e S-1210 para transportadores autônomos cadastrado no módulo de Gestão Financeira que tem desconto SEST e SENAT?](http://tdn.totvs.com/pages/releaseview.action?pageId=397382319)  
- [Quais autônomos do TOTVS Gestão Financeira são considerados na geração do S-1200 e S-1210?](https://tdn.totvs.com/pages/releaseview.action?pageId=782315485)   
- [Como gerar S-1200 para Autônomos do Fluxus todas as categorias?](https://tdn.totvs.com/pages/releaseview.action?pageId=440855187)   
- [Autônomos e Externos 1/2](https://tdn.totvs.com/pages/releaseview.action?pageId=452719944)   
- [Autônomos e Externos 2/2](https://tdn.totvs.com/pages/releaseview.action?pageId=463823367)
