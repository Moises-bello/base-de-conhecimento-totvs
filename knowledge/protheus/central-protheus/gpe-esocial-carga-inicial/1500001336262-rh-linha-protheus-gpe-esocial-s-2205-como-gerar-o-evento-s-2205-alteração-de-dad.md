---
article_id: 1500001336262
category: GPE - eSocial - Carga Inicial
content_hash: 7fd050672dbaa3c9aeb8661178c48d376d7797b68427cdfe45572a0ea1bb7f6b
fetched_at: '2026-06-28T22:45:03.337344+00:00'
product: protheus
section_id: 360005445833
source: central-protheus
title: RH - Linha Protheus - GPE - eSocial - S-2205 - Como gerar o evento S-2205 (Alteração
  de Dados Cadastrais do Trabalhador)
type: support-article
updated_at: '2025-11-27T21:36:34Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/1500001336262-RH-Linha-Protheus-GPE-eSocial-S-2205-Como-gerar-o-evento-S-2205-Altera%C3%A7%C3%A3o-de-Dados-Cadastrais-do-Trabalhador
---

**Dúvida**  
Como gerar o evento **S-2205 Alteração Cadastral** no eSocial?  
  
**Ambiente**  
TOTVS RH - TOTVS RH (Linha Protheus) - Gestão de Pessoal - Todas as Versões  
  
**Solução**  
O evento **S-2205** (Alteração de Dados Cadastrais do Trabalhador) registra as alterações de dados cadastrais do trabalhador, tais como: documentação pessoal, endereço, escolaridade, estado civil, dependentes, etc. Deve ser utilizado tanto para empregados/servidores, inseridos através do evento S-2200, quanto para outros trabalhadores sem vínculo de emprego cujas informações foram enviadas originalmente através do evento específico de “S-2300 - Trabalhador Sem Vínculo de Emprego/Estatutário – Início”.  
  
No Protheus é possível gerar o **S-2205** (Alteração de Dados Cadastrais do Trabalhador), fazendo alterações no **cadastro do funcionário** (GPEA010), ou no **cadastro do dependente** (GPEA020). Para saber os campos que fazem parte do evento S-2205 consulte o *link*: [**Eventos S-2205 De / Para de campos Protheus com layout eSocial**](https://tdn.totvs.com/pages/viewpage.action?pageId=286518482).  
  
Abaixo segue um exemplo de como efetuar a geração do evento **S-2205** e transmissão para o governo no **TAF**.

**HOW TO - SIGAGPE - Integrando o evento S-2205**  
  
  
**Observações**  
**1)** O evento **S-2205** só é gerado caso o evento **S-2200** (Cadastramento Inicial do Vínculo e Admissão/Ingresso do Trabalhador), esteja no governo.  
  
**2)**O evento S-2205 somente será gerado quando o trabalhador estiver ativo devido a regra de validação do eSocial de recepção dos eventos em ordem cronológica. Caso precise realizar alteração após o desligamento do trabalhador, orientamos que exclua a rescisão e realize a alteração necessária.  
  
**3)** Alteração do PIS não gera o evento S-2205 pois o governo retirou essa informação do leiaute  
  
**4)** O Evento de S-2205 - Alteração Cadastral deve ser gerado quando dados cadastrais do funcionário são alterados :  
  
Cadastro de Funcionários (GPEA010) ou Cadastro de Dependentes (GPEA020) - Operação ALTERAÇÃO.  
Caso um dos campos abaixo seja alterado:

* Nome (RA\_NOMECMP)
* Sexo(RA\_SEXO)
* Raça e cor (RA\_RACACOR)
* Estado Civil (RA\_ESTCIVI)
* Grau de instrução (RA\_GRINRAI)
* Nome Social (RA\_NSOCIAL) Tipo de logradouro (RA\_LOGRTP)
* Pais de origem (RA\_NACIONC)
* Tipo de Logradouro (RA\_LOGRTP)
* Descrição logradouro (RA\_LOGRDSC)
* Numero do logradouro (RA\_LOGRNUM)
* Complemento (RA\_COMPLEM)
* Bairro (RA\_BAIRRO)
* CEP (RA\_CEP)
* Código Município (RA\_CODMUN)
* Estado (RA\_ESTADO)
* Pais de Res. Exterior (RA\_PAISEXT)
* Tempo Residência Estrangeiro (RA\_TIPOVIA)
* Classif Estrangeiro (RA\_CLASEST)
* Portador de deficiência(RA\_PORTDEF)
* E-mail (RA\_EMAIL)
* Telefone (RA\_DDDFONE + RA\_TELEFON)
* Dados dos Dependentes

**Atenção:** Caso o parâmetro MV\_OPESOC esteja habilitado, o sistema não gera as informações no evento S-2205 pois entende que a alteração deve gerar os eventos de Entes Públicos como S-2400 / S-2405.  
  
O parâmetro deve ficar **desabilitado** caso seja necessário **gerar o evento S-2205**.  
  
**Saiba Mais**  
Para saber mais consulte os *links* abaixo:  
[eSocial | Protheus - Entregas Legais](http://tdn.totvs.com/x/4JQYEw)  
[MOS - Manual de Orientação eSocial](https://www.gov.br/esocial/pt-br/documentacao-tecnica/documentacao-tecnica)  
[Perguntas Frequentes site eSocial](https://www.gov.br/esocial/pt-br/empresas/perguntas-frequentes/perguntas-frequentes)   
[ChatBot Carol Assistant](https://centraldeatendimento.totvs.com/hc/pt-br/articles/360022200991)  
  
*Para conhecimento dos eventos futuros, acessa a nossa página*[***TOTVS Informa***](https://informa.totvs.com/)*selecione em categorias a área e pesquise por "****Eventos****".*
