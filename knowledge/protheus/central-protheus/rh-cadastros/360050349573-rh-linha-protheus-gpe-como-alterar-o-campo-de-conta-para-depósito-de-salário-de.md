---
article_id: 360050349573
category: RH - Cadastros
content_hash: b15480d2aa7967966115b2b5e3a6e6f16d24ef36e88cd0b3dbb7e2c39273aefb
fetched_at: '2026-06-28T22:43:25.846492+00:00'
product: protheus
section_id: 360010781894
source: central-protheus
title: RH - Linha Protheus - GPE - Como alterar o campo de conta para depósito de
  salário de numérico para alfa numérico
type: support-article
updated_at: '2026-06-25T12:44:57Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050349573-RH-Linha-Protheus-GPE-Como-alterar-o-campo-de-conta-para-dep%C3%B3sito-de-sal%C3%A1rio-de-num%C3%A9rico-para-alfa-num%C3%A9rico
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/16532233529111) Tempo aproximado para leitura: **00:02:00 min**

**Dúvida**  
Como alterar o campo de conta para depósito de salário de numérico para alfa numérico?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**

Para alterar o campo da rotina de numérico para alfa numérico, realize os seguintes passos:

1. Identifique o nome do campo. Para isso, clique sobre o campo no cadastro de funcionário e pressione F1 - **campo: RA\_CTDEPSA.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073578263)  
  
**2.** Acesse pelo Configurador SIGACFG **Base de dados > Dicionário > Base de dados**

**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073585687)**

**3.** **Clique** no **Expandir a tabela ()** depois em **Dicionários de Dados** deixe carregar as tabelas e clique na **Lupa**e busque pela SRA. Depois, clique em editar.  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073597079)**  
  
**4.** Clique no **expansor** ao lado do nome da tabela (Funcionários) e selecione a opção campos. Busque pelo campo **RA\_CTDEPSA** no ícone da **lupa** e depois clique em **editar** (ícone de folha com lápis).  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073607319)

**7.** Na Campo em **Formato,** digite  a nova configuração do campo  **@!** e clique em **Salvar.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073614359)  
  
**8.** Na tela da listagem de tabelas, clique em **Atualizar base de dados**(ícone de disquete). Clique em **avançar** e depois **finalizar.**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073616791)  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073618967)  
  
**Importante:**  
O processo de **Atualizar Base de Dados** tem por finalidade **confirmar** a inclusão do campo na tabela no banco de dados. Este procedimento deve ser feito em **modo exclusivo,** ou seja, **não** pode haver **nenhum usuário** com alguma rotina aberta que utilize a tabela envolvida.  
  
**9.** Acesse o cadastro do funcionário e altere o numero da conta com números e letras e confirme.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/26573073621527)

**Saiba Mais**  
[RH - Linha Protheus - GPE - Como retirar validação da tabela SA6 - Bancos/Agências do campo RA\_BCDEPSA](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360035730393-RH-Linha-Protheus-GPE-Como-retirar-valida%C3%A7%C3%A3o-da-tabela-SA6-Bancos-Ag%C3%AAncias-do-campo-RA-BCDEPSA?source=search)  
[RH - Linha Protheus - GPE - Como cadastrar banco/agência com dígito verificador X](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360052965754-RH-Linha-Protheus-GPE-Como-cadastrar-banco-ag%C3%AAncia-com-d%C3%ADgito-verificador-X?source=search)
