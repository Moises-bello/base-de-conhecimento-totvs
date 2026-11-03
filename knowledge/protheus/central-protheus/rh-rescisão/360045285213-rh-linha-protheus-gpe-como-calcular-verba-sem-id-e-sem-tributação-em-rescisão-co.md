---
article_id: 360045285213
category: RH - Rescisão
content_hash: 777d147073e6664b7e8e88fb5d09092847f434b4980ede94a4e234581454b47a
fetched_at: '2026-06-28T22:43:52.011301+00:00'
product: protheus
section_id: 360001597331
source: central-protheus
title: RH - Linha Protheus - GPE - Como calcular verba sem ID e sem tributação em
  rescisão complementar para pagamento de PLR
type: support-article
updated_at: '2025-07-17T12:28:42Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360045285213-RH-Linha-Protheus-GPE-Como-calcular-verba-sem-ID-e-sem-tributa%C3%A7%C3%A3o-em-rescis%C3%A3o-complementar-para-pagamento-de-PLR
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/33530515893527) Tempo aproximado para leitura: **00:01:00 min  
  
Dúvida**No cálculo da rescisão complementar com pagamento (provento) somente de PLR o sistema não efetua a geração da verba de desconto sem id lançada na RGB.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - A partir da versão 12.1.17  
  
**Solução**Foi realizada a criação do campo RV\_REFPLR no cadastro de verbas, para definir se a verba informada em questão será ou não gerada na rescisão complementar por PLR, para isso, realize os procedimentos abaixo:

* Criar via configurador o campo conforme abaixo:  
    
  ![mceclip0.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062398533)

Para a criação do campo realize os seguintes passos:

* Acesse o Configurador com senha de Administrador em modo exclusivo, através do menu **Base de Dados > Dicionário > Base de Dados.**
* Clique na **Empresa** para **expandir** as opções. Selecione **Dicionário de Dados** e clique na lupa para busca de tabela.
* Busque pela tabela **SRV**, selecione a opção e clique em editar.
* Clique em **Verbas** para expandir as opções, selecione a opção **Campos** e clique no ícone de **folha com +** para incluir um novo campo
* Configure o campo conforme desejado e clique em **salvar**.
* Clique no ícone do disquete para que o sistema atualize o diconário de dados com o novo campo criado

3. Após criação do campo, na verba que será lançada na rescisão complementar para pagamento de PLR, neste campo deverá ficar com Sim conforme abaixo:  
  
![mceclip1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/360062402653)

**Saiba Mais:**

[RH - Rescisão](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597331-RH-Rescis%C3%A3o)
