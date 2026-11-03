---
article_id: 360016062132
category: Fiscal Arquivos Magnéticos - SPED Contribuições
content_hash: d07754fd25f92046ce3edb9bdaecb7e195305c114e4c8bf0edac0c84cd0e7730
fetched_at: '2026-06-28T22:42:06.712726+00:00'
product: protheus
section_id: 1500001535081
source: central-protheus
title: Cross Segmentos - Backoffice Protheus - FIS - Arq.Magnéticos - Tabela CG1 -
  Como importar no sistema a Tabela 5.1.1 (Código de Atividade, Produtos e Serviços
  Incidentes da Contribuição Sobre a Receita Bruta)
type: support-article
updated_at: '2025-02-12T13:08:55Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360016062132-Cross-Segmentos-Backoffice-Protheus-FIS-Arq-Magn%C3%A9ticos-Tabela-CG1-Como-importar-no-sistema-a-Tabela-5-1-1-C%C3%B3digo-de-Atividade-Produtos-e-Servi%C3%A7os-Incidentes-da-Contribui%C3%A7%C3%A3o-Sobre-a-Receita-Bruta
---

**Dúvida**Com as alterações na **NT 009 do EFD Contribuições**, a **Receita Federal** publicou o fim da geração dos **registros 0145 e Bloco P** referente ao **CPRB** no **EFD Contribuições**.   
Porém, a tabela **CG1** ainda é utilizada para a geração da **REINF**A nova tabela disponibilizada no portal do **Sped** relacionada a **CPRB** **(Contribuição Previdenciária sobre a Receita Bruta)** passou a ter uma estrutura nova. Ao importar esta nova tabela o sistema não está atualizando os dados corretamente.

Conforme alteração realizada na **NT 05-2024**, a partir de **janeiro de 2025** será alterada as alíquotas da **CPRB** com redução gradual, seguindo um cronograma liberado pela receita na **NT 05-2024**.

*Link* da nota técnica: **NOTA TÉCNICA EFD-REINF 05/2024 ( sped.rfb.gov.br )**

Mais Informações: <https://tdn.totvs.com/pages/releaseview.action?pageId=910024556>

Como importar no sistema a **Tabela 5.1.1 REINF - (Tabela de Código de Atividades, Produtos e Serviços Sujeitos à Contribuição Sobre a Receita Bruta)?**

**Ambiente**Microsiga Protheus – Livros Fiscais – A partir da versão 2310  
  
**Solução**  
Para solucionar essa dúvida, realize os seguintes passos:

1. Realize o *download* da Tabela do **REINF** em: <http://www.sped.fazenda.gov.br/spedtabelas/AppConsulta/publico/aspx/ConsultaTabelasExternas.aspx?CodSistema=reinf> 

![CPRB 1.png](https://centraldeatendimento.totvs.com/hc/article_attachments/29930342326423)

2. Para que o arquivo baixado seja importado, renomeei para **TABELA511.TXT** (o arquivo obrigatoriamente deve ter este nome).Depois, salve o arquivo na pasta **ARQSPED**, que deve ser criada manualmente dentro da pasta **PROTHEUS\_DATA\SYSTEM**

3. Execute o **compatibilizador U\_IMPSPED** e selecione a pasta **ARQSPED** criada anteriormente.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/360011995952)

3. Existe também a opção de importar pela opção **Importação Códigos EFD** dentro da Rotina **FISA001**Acesse a **Apuração da EFD Contribuições** (Rotina FISA001) e clique na opção **Importação Códigos EFD**:

![TESTEGIF3.gif](https://centraldeatendimento.totvs.com/hc/article_attachments/360011996052)

Observação.: A tabela que será atualizada no sistema recebendo os códigos de atividade é a **tabela CG1**.
