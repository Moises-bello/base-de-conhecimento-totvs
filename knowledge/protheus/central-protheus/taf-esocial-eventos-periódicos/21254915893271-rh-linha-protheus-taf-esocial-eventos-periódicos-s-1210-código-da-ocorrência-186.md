---
article_id: 21254915893271
category: TAF - eSocial - Eventos Periódicos
content_hash: 230e1c142d0d5e1344796d4bdabc0bf1c5cafabf0770222468e7a0acea17e17a
fetched_at: '2026-06-28T22:45:19.068349+00:00'
product: protheus
section_id: 1500001536901
source: central-protheus
title: 'RH - Linha Protheus - TAF - eSocial - Eventos Periódicos - S-1210 -  Código
  da Ocorrência 186: CPF do dependente xxxxxxxxxxx invalido. Ação sugerida: Deve ser
  um CPF de dependente cadastrado no RET do eSocial ou no grupo de informações de
  Dependentes do'
type: support-article
updated_at: '2026-06-25T12:24:11Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/21254915893271-RH-Linha-Protheus-TAF-eSocial-Eventos-Peri%C3%B3dicos-S-1210-C%C3%B3digo-da-Ocorr%C3%AAncia-186-CPF-do-dependente-xxxxxxxxxxx-invalido-A%C3%A7%C3%A3o-sugerida-Deve-ser-um-CPF-de-dependente-cadastrado-no-RET-do-eSocial-ou-no-grupo-de-informa%C3%A7%C3%B5es-de-Dependentes-do
---

![time.png](https://centraldeatendimento.totvs.com/hc/article_attachments/21254905837207) Tempo aproximado para leitura: **00:05:00 min****Ocorrência****Ao tentar transmitir o evento S-1210 (Pagamentos de Rendimento) ao eSocial é retornada a inconsistência abaixo:  
  
Sequência 000001 - Tipo: Erro - Código da Ocorrência 186  
Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/planSaude[1]/infoDepSau/cpfDep  
Descrição: CPF do dependente xxxxxxxxxxx invalido. Ação sugerida: Deve ser um CPF de dependente cadastrado no RET do eSocial ou no grupo de informações de Dependentes do próprio evento.****Ambiente**TOTVS RH - TOTVS RH (Linha Protheus) - eSocial - TAF - Todas as versões.  
  
**Causa**O eSocial não localizou o CPF do dependente (especificado no erro) dentro do Portal do eSocial para a competência do evento.  
  
**Solução**Para corrigir o erro:  
**1.** Verifique se os **dependentes estão devidamente cadastrados** em seu **ERP de origem** (Protheus Recursos Humanos, RM Labore, Datasul, Logix, etc.);  
  
**2.**  Com os dependentes cadastrados devidamente no **EPR de origem**, gere um evento **S-2205** para o colaborador que está apresentando erro na transmissão do S-1210. Dessa forma o cadastro dos dependentes serão atualizados no TAF e no eSocial.  
  
**3.** Realize a transmissão do evento S-2205 para o eSocial.  
  
**Importante:** O evento **S-2205** deve ter data de início (competência) **igual ou anterior a data do evento S-1210**, nunca superior.  
  
**4.** Após a transmissão com sucesso do evento **S-2205,** transmita novamente o evento **S-1210**.  
  
**Documentações relacionadas:**

* [RH - Linha Protheus - GPE - eSocial - S-1210 - Inconsistência retornada pelo RET: Codigo da ocorrência: 186 Localização: /eSocial/evtPgtos/ideBenef/infoIRComplem/infoIRCR/dedDepen[1]/cpfDep](https://centraldeatendimento.totvs.com/hc/pt-br/articles/19819208680215)
* [RH - RM - FOP - eSocial - Erro na geração do XML: O campo 'cpfDep' do registro 'dependente' é obrigatório e não está preenchido](https://centraldeatendimento.totvs.com/hc/pt-br/articles/6296717756951)

**Saiba Mais**Para saber mais consulte os links abaixo:   
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e**pesquise**por "****Eventos****"*Essa documentação também pode ser acessada 24h por dia e pelo Protheus, através da Carolina: [Carolina - Assistente Virtual - Como usar a Carolina pelo ícone no produto Protheus](https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500008685602-Carolina-Assistente-Virtual-Como-usar-a-Carolina-pelo-%C3%ADcone-no-produto-Protheus-)
