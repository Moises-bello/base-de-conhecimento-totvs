---
article_id: 360062332213
category: RH - 13º salário
content_hash: 31635bdb938e653c97ddc095cdd0642459278472e466fe5673b48d1ff896e436
fetched_at: '2026-06-28T22:44:00.733411+00:00'
product: protheus
section_id: 360001597271
source: central-protheus
title: RH - Linha Protheus - GPE - Complemento 13º negativo impede a transmissão do
  S-1200
type: support-article
updated_at: '2025-08-13T13:59:30Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360062332213-RH-Linha-Protheus-GPE-Complemento-13%C2%BA-negativo-impede-a-transmiss%C3%A3o-do-S-1200
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/18959906715543) Tempo aproximado para leitura: **00:03:00 min**  
**Ocorrência**Complemento 13º negativo impede a transmissão do S-1200.  
  
**Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as versões  
  
**Causa**Ao calcular complemento 13º do tipo desconto (Id 0348), o sistema gera as bases de INSS/FGTS negativas e consequentemente estes valores são levados no S-1200, porém o RET não aceita valores negativos.

**Solução**No caso de complemento negativo de 13º salário devido a perda de avos por exemplo e com o parâmetro **MV\_DF13NEG = 'S' e P\_CCOMP13 = 'S'**, são geradas verbas negativas de INSS, IR e FGTS, para que isso não ocorra foram criados novos Identificadores de cálculos para gerar esses valores como base e no caso do IR e INSS como provento para o funcionário.

Realizamos consultoria jurídica a respeito e tivemos um retorno sobre a devolução do INSS em folha ao funcionário, cabendo à empresa posterior pedido de ressarcimento através do PERD/COMP.

Para que o sistema acate essa nova configuração basta cadastrar novas verbas para os Id's abaixo, é preciso que todos eles sejam cadastrados com as mesmas configurações das verbas da coluna de "ID referência", caso contrário o sistema continuará gerando as verbas originais com valores negativos.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/23155976087447)  
  
Para cadastrar esses novos identificadores de cálculo, acesse **Atualizações > Definições de cálculo > Verbas GPEA040** e clique em **Incluir**.

OBS. Os **Ids 1674 e 1675** foram desativados porque a consultoria disponível no endereço [IRRF - Pago Indevidamente ou a Maior no 13º Salário](https://tdn.totvs.com/pages/viewpage.action?pageId=663060963) afirma que não pode haver devolução de IR pelo empregador.

**Importante**

As incidências de eSocial das verbas são apenas sugestões, o usuário precisa analisar em seu ambiente, as verbas que compõem ou não as bases de IR, INSS e FGTS e configurar as incidências para o eSocial de acordo.

Verifique também a criação do ID 1679 Pensão de 13 salário negativa: RH - [Linha Protheus - GPE - Pensão de 13 salário negativa no complemento do 13º Salário, criação id 1679](https://centraldeatendimento.totvs.com/hc/pt-br/articles/4414523041943-RH-Linha-Protheus-GPE-Pens%C3%A3o-de-13-sal%C3%A1rio-negativa-no-complemento-do-13%C2%BA-Sal%C3%A1rio-cria%C3%A7%C3%A3o-id-1679?source=search)

**Saiba Mais**

[RH - 13º salário](https://centraldeatendimento.totvs.com/hc/pt-br/sections/360001597271-RH-13%C2%BA-sal%C3%A1rio)

Boletim Técnico: <https://tdn.totvs.com/pages/releaseview.action?pageId=469452222>

O sistema deve estar atualizado para que as verbas possam ser criadas:  
<https://suporte.totvs.com/portal/p/10098/download#all/all/all/search/rh_expedicao>
