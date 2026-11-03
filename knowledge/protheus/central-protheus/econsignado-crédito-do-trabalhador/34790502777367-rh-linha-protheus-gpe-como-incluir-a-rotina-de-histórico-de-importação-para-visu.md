---
article_id: 34790502777367
category: eConsignado (Crédito do Trabalhador)
content_hash: cc37121d8df1aa2b0bc2e61b0d943363c8cf6080c6f37b5343288905d168be70
fetched_at: '2026-06-28T22:43:07.227157+00:00'
product: protheus
section_id: 32292829000215
source: central-protheus
title: RH - Linha Protheus - GPE - Como incluir a rotina de Histórico de Importação
  para visualização de todas as importações do eConsignado realizadas
type: support-article
updated_at: '2025-09-15T17:20:45Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/34790502777367-RH-Linha-Protheus-GPE-Como-incluir-a-rotina-de-Hist%C3%B3rico-de-Importa%C3%A7%C3%A3o-para-visualiza%C3%A7%C3%A3o-de-todas-as-importa%C3%A7%C3%B5es-do-eConsignado-realizadas
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/34790502759447) Tempo aproximado para leitura: **00:01:30 min**  
  
**Dúvida**  
Como consultar Importações do eConsignado referente ao mês seguinte a folha ainda aberta  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - TOTVS Gestão de Pessoal - a partir da versão 12.1.2210  
  
**Solução**  
Para consultar o **Histórico completo**, e ver todas as importações realizadas (mês atual e mês seguinte), será necessário incluir no menu a rotina **GPEM944A** - **Histórico Crédito Trabalhador**

Para incluir a rotina, acesse o SIGACFG - Configurador - com senha de Administrador pelo menu **Ambiente → Cadastros → Menus**  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948410070551)  
  
Selecione apenas a opção **Gestão de Pessoal** e clique em **Ok**.  
**Obs.:** Caso tenha algum item incluído, a opção aparecerá como **Gestão de Pessoal** **- Personalizado**, conforme exemplo abaixo:  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948388463639)  
  
Clique em **adicionar** e deixe carregar.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948388466071)

Selecione a opção Atualizações e depois clique em **Novo Grupo**. Preenche aos três campos (Português, Inglês e Espanhol) e clique em **Ok.**

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948388467735)

Selecione o novo grupo criado e depois clique em **Novo Item** para adicionar as informações da rotina.  
  
**Desc. Português**: Histórico de Importação  
**Programa**: GPEM944A  
**Módulo**: Gestão de Pessoal  
**Tipo**: Função Protheus  
  
Após o preenchimento, clique em **Ok** para confirmar a inclusão.

![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948388469271)  
  
Clique em **Gerar**, informe **SIGAGPE** no campo arquivo e depois **Gerar** para concluir a inclusão no menu.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948410081431)  
  
Saia do Sistema e acesse novamente para que a alteração no menu do SIGAGPE seja atualizada.  
  
Acesse no SIGAGPE o menu → **Atualizações → Crédito do Trabalhador → Histórico Crédito Trabalhador.**  
  
**![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948410083351)**  
  
**Observação**: O caminho indicado é uma **sugestão**, então fica a critério do usuário a localização que deseja incluir a rotina no menu do SIGAGPE.  
  
Na rotina serão apresentados todos os dados gravados na **RUO - Histórico de Importações**.  
  
![](https://centraldeatendimento.totvs.com/hc/article_attachments/34948681578519)  
  
  
**Saiba Mais**

[RH - Linha Protheus - GPE - Na consulta do Histórico de Importações do eConsignado em Valores Futuros, Sistema emite alerta: Não existem importações no histórico que correspondam à verba selecionada](https://centraldeatendimento.totvs.com/hc/pt-br/articles/34944956182551-RH-Linha-Protheus-GPE-Na-consulta-do-Hist%C3%B3rico-de-Importa%C3%A7%C3%B5es-do-eConsignado-em-Valores-Futuros-Sistema-emite-alerta-N%C3%A3o-existem-importa%C3%A7%C3%B5es-no-hist%C3%B3rico-que-correspondam-%C3%A0-verba-selecionada)

[Manual do Crédito Consignado do Trabalhador](https://www.gov.br/trabalho-e-emprego/pt-br/servicos/empregador/fgtsdigital/manual-e-documentacao-tecnica/manual-operacional-do-empregador-programa-credito-do-trabalhador-v2-16-05-25.pdf)

[Orientações Consultoria de Segmentos - Crédito do Trabalhador](https://tdn.totvs.com/pages/releaseview.action?pageId=939253541#Orienta%C3%A7%C3%B5esConsultoriadeSegmentosCr%C3%A9ditodoTrabalhador-3.7.2Ovalordoabonopecuni%C3%A1riodevecomporaremunera%C3%A7%C3%A3odispon%C3%ADvelparadescontodocr%C3%A9ditodotrabalhador?)

[Manual Crédito do Trabalhador Protheus](https://tdn.totvs.com/pages/releaseview.action?pageId=944703898)

[eConsignado (Crédito do Trabalhador)](https://centraldeatendimento.totvs.com/hc/pt-br/sections/32292829000215-eConsignado-Cr%C3%A9dito-do-Trabalhador)
