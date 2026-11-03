---
article_id: 360050962133
category: RH - Folha de Pagamento
content_hash: c550756dc2e85af95e1b60e25c53dc2f1c5e425e56035702bad6984d6fe456e7
fetched_at: '2026-06-28T22:44:12.148917+00:00'
product: protheus
section_id: 206960867
source: central-protheus
title: RH - Linha Protheus - GPE - Campos Periculosidade e Insalubridade não gravam
  o conteúdo informado no cadastro de Funcionário
type: support-article
updated_at: '2025-08-22T19:47:33Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360050962133-RH-Linha-Protheus-GPE-Campos-Periculosidade-e-Insalubridade-n%C3%A3o-gravam-o-conte%C3%BAdo-informado-no-cadastro-de-Funcion%C3%A1rio
---

**![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/26356877894935) Tempo aproximado para leitura: 00:03:00 min**

**Dúvida**Campos **Periculosidade** e **Insalubridade** **não gravam o conteúdo** informado no cadastro de Funcionário  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**Quando isso ocorrer, verifique por favor se o parâmetro **MV\_MDTGPE** está habilitado, pois isso normalmente ocorre quando o GPE tem integração com o MDT. Quando existe essa integração, os adicionais de **Periculosidade e Insalubridade, devem vir do cadastro de Riscos do MDT**, por isso que **pelo GPE, o sistema não grava o ajuste direto** ou altera no Fechamento, e quando desativa o parâmetro aceita o preenchimento e não altera quando fechar o mês.  
  
Veja a documentação abaixo:  
[https://tdn.totvs.com/display/PROT/MDT0044\_Periculosidade\_Insalubridade\_Cadastro\_do\_Funcionario](https://www.google.com/url?q=https://tdn.totvs.com/display/PROT/MDT0044_Periculosidade_Insalubridade_Cadastro_do_Funcionario&sa=D&source=hangouts&ust=1570199300441000&usg=AFQjCNFqUTT97EaQ6nNllfqj-v9HrdBHBA)  
  
Após avaliar a documentação acima, deve **definir qual a melhor forma de trabalhar.**  
  
Por exemplo:   
  
Deixando o **MV\_MDTGPE desabilitado**, não integrará os dados com o MDT realmente, porém **conseguirá preencher a periculosidade direto no cadastro do funcionário**  
  
Deixando o **MV\_MDTGPE habilitado**, integrará os dados com o MDT, porém, **não conseguirá simplesmente preencher a periculosidade direto no cadastro de funcionário**, pois como expliquei anteriormente, quando há integração com o MDT, **os adicionais de Periculosidade por exemplo, devem vir do cadastro de Riscos do MDT**, por isso que pelo GPE, o sistema não grava o ajuste direto e quando desativa, aceita o preenchimento. 

**Saiba Mais**

[RH - Protheus - Folha de Pagamento](https://centraldeatendimento.totvs.com/hc/pt-br/sections/206960867-RH-Folha-de-Pagamento)

[RH - Linha Protheus - GPE - Como fazer o download (baixar) do pacote de expedição contínua (acumulado) do RH Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360057829854-RH-Linha-Protheus-GPE-Como-fazer-o-download-baixar-do-pacote-de-expedi%C3%A7%C3%A3o-cont%C3%ADnua-acumulado-do-RH-Protheus)
