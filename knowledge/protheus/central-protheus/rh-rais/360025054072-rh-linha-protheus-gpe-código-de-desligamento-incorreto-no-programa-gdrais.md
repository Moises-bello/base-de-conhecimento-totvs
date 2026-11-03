---
article_id: 360025054072
category: RH - RAIS
content_hash: 477a852c267109598e074af456e9b47a8146750c7a6b5997d47b95e4a0f6137e
fetched_at: '2026-06-28T22:44:05.730405+00:00'
product: protheus
section_id: 360000030327
source: central-protheus
title: RH - Linha Protheus - GPE - Código de desligamento incorreto no programa GDRAIS
type: support-article
updated_at: '2022-03-23T20:31:38Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360025054072-RH-Linha-Protheus-GPE-C%C3%B3digo-de-desligamento-incorreto-no-programa-GDRAIS
---

**Dúvida**Ao importar o arquivo .txt no programa GDRAIS o código de desligamento está incorreto, onde corrigir?  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal –A partir da versão 12.1.17  
  
**Solução**Essa informação passa por algumas rotinas antes de chegar no programa GDRAIS e por esse motivo a informação terá que ser mapeada em sua base:  
  
**1**. Entre na **rescisão do funcionário** e veja qual foi o código de rescisão utilizado (Miscelânea/ Cálculo/ Rescisão/ Campo Tipo Resc);  
**2**. Entre no cadastro do **tipo de rescisão** utilizado e veja o conteúdo da coluna Cód. Resc. Rais (Atualizações/ Definições Calculo/ Manutenção Tabelas/ S043/ Coluna Cód. Resc. Rais), anote esse conteúdo;  
**3**. Verifique se o campo Cód. Resc. Rais, localizado dentro do **Cadastro de Funcionário** está com o mesmo conteúdo da coluna Cód. Resc. Rais do tipo de rescisão utilizado;  
**4**. Após a geração da RAIS, entre na **Manutenção Arquivo** e busque pelo campo Cód. Resc. Rais. O código informado nesse campo deve ser o mesmo do tipo de rescisão (Item 2) e do cadastro do funcionário (Item 3);  
**5**. Por último, veja qual o código foi gerado no arquivo TXT - posição 157 a 158.  
  
Se até o passo 3 os códigos estiverem corretos, por favor excluir as informações do funcionário na rotina **Manutenção Arquivo** e gerar novamente apenas para essa matrícula através da rotina **Geração Arquivo**.

**Saiba mais**  
Para verificar as dúvidas mais frequentes sobre a RAIS, acesse o *link*abaixo:  
<https://centraldeatendimento.totvs.com/hc/pt-br/sections/360000030327-RH-RAIS>
