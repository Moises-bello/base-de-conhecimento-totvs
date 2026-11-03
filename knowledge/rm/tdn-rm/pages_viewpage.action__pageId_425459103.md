---
content_hash: 6288f3a7c00fe78245fb97960d4ef13ea54e240c9eb00e16ed9fbaecaf3b8d5e
fetched_at: '2026-06-29T00:09:33.984999+00:00'
page_id: '425459103'
product: rm
source: tdn-rm
title: Integração com Totvs Educacional
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459103
version: 1
---

**Integração com Totvs Educacional**

---

A integração possibilita o aluno acompanhar, através do Portal do Educacional, os atendimentos abertos durante todos os períodos letivos. Esta funcionalidade permite maior interação com os sistemas gerando comodidade durante todo processo de duração da ocorrência.  
**Desenvolvimento/Procedimentos**  
1.     Incluir Solicitação de Atendimento através do Classis.  
Acesse: Atendimentos / Solicitação de Atendimento através do RM Classis.  
2.     Preencher Seleção de Contexto:

* Incluir Nível de Ensino para ser utilizado dentro dos serviços da área Educacional.
* Definir Valores de Contexto através da validação das configurações atuais que vão ser utilizadas em todo o sistema.
* Informar a Descrição do Processo (Optativo).

3.     Parametrizar os Dados do Atendimento:

* Incluir Grupo de Atendimento.
* Incluir Tipo de Atendimento.

4.     Parametrizar os Dados do Aluno:

* Validar Período Letivo (Por default o sistema busca o período informado como corrente).
* Informar o aluno.
* Incluir o Contrato no Período Letivo.
* Incluir a Matrícula do Período Letivo.

5.     Preencher as informações do  atendimento:

* Dados da Solicitação: Nome , Localidade (Obrigatório), Justificativa (Obrigatório).
* Descrição: Informações complementares.
* Descrição Detalhada: Informações complementares.
* Procedimentos: Informações complementares.
* Aceite: Informações complementares.

**Descrição do Processo**

* Após efetuar as parametrizações citadas acima, execute o processo.
* Verifique o atendimento.
* Acesse:

               Anexo | Informações do Aluno  
               Anexo| Informações Estratégicas | Anexos | Informações do Aluno  
Verifique os dados extras relacionados ao aluno informado na ocorrência.

* Nos anexos, o ícone  é apresentado com o objetivo de destacar o período letivo no qual o atendimento foi aberto. Obs.: O aluno pode estar matriculado em vários períodos diferentes.

**Informações Adicionais**  
As configurações necessárias para o funcionamento da integração devem ser parametrizadas no RM Classis:  
Secretaria | Integração CRM | Configurações:

* Tipo de Atendimento

Opções | Parâmetros | Totvs Educacional | Integração | Atendimento:

* Parametrizar = Atendimento Geral 1

                                 Atendimento Geral 2                                            
As solicitações de atendimentos através do Classis podem ser verificadas via Web, o que facilita o acompanhamento e a abertura de atendimentos de qualquer lugar que possua acesso a internet.

|  |  |
| --- | --- |
|  | Recursos Adicionais |

---

[Blog - Integração com Educacional](http://totvsconnect.blogspot.com/2010/11/como-fazer-integracao-crmrm-agilis-x_29)
