---
content_hash: eda17583012c3689e4a4cf3b25888365aa62624b7dd951f81572a00280717001
fetched_at: '2026-06-29T00:09:34.059098+00:00'
page_id: '425459127'
product: rm
source: tdn-rm
title: Estágio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=425459127
version: 13
---

---

**Estágio 1/7: Parâmetros Gerais**

* Qual é o número de alunos que cada professor pode orientar.
* Número de alunos que podem ser supervisionados por uma mesma pessoa na empresa.
* Permite ao aluno informar pelo portal a empresa ou funcionário que não estejam cadastros.
* Na solicitação de estágio, caso o funcionário que esteja sendo cadastrado seja Responsável Legal, obriga o preenchimento dos campos CPF, RG e endereço.

**Estágio 2/7: Parâmetros Gerais**

* Aluno poderá concorrer a uma vaga em caso de choque de horário?
* Relatório de Termo de Encaminhamento: Assim que o aluno for selecionado, o mesmo poderá receber via e-mail o Termo de Encaminhamento.
* O armazenamento dos arquivos poderá ser feito em base de dados, algum diretório da rede bem como no TOTVS ECM. É possível restringir o tamanho dos arquivos bem como as suas extensões.

falseIMPORTANTE!!!

**Para as Versões 12.1.34 e anteriores.**  
Se a Instituição de ensino, tiver parametrizado o tipo de Armazenamento como: "Arquivo de algum diretório" e informar um diretório para armazenamento, o mesmo será exclusivo para os arquivos que envolve a rotina de Central de Estágio.

falseIMPORTANTE!!!

**A partir da Versão 12.1.2209**  
Se a Instituição de ensino, tiver parametrizado o tipo de Armazenamento como: "Arquivo de algum diretório" deverá ser informado o **nome do diretório** (caso estiver com **multitenant habilitado**) ou o **caminho do diretório** (caso estiver com o **multitenant desabilitado**).

**Exemplo** quando o **multitenant** estiver **habilitado**: Imagens\Documentos → esse é o nome do diretório e subdiretório onde os arquivos serão salvos. *Não colocar caminho de pasta  →  ex: c:\arquivos.*

Referência:

**Exemplo** quando o **multitenant** estiver **desabilitado**: C:\Imagens\Documentos → esse é o caminho do diretório e subdiretório onde os arquivos serão salvos.

**Estágio 3/7: Seleção Estágio**

* Relatório para incluir como anexo ao email de notificação o aluno selecionado para a vaga.
* Número de dias após a seleção do aluno para preenchimento do plano de atividade.

**Estágio 4/7: Termo de Compromisso**

* É possível associar a um relatório o Termo de Compromisso que será encaminhado via e-mail aos alunos.
* Duração máxima do estágio bem como a carga horária semanal máxima.

**Estágio 5/7: Plano de Atividade**

* Número de dias para aprovação do plano de atividade após envio por parte do aluno.
* Permitir ao aluno alterar o plano de atividade após aprovação do professor.
* Solicita que o supervisor do estágio aprove o plano de atividade e suas etapas.

**Estágio 6/7: Avaliação final**

* O Aluno visualiza a avaliação final informada pelo supervisor da empresa.
* O Professor visualiza a avaliação final informada pelo supervisor da empresa.

**Estágio 7/7: Fórmulas visuais do estágio**

* Possibilita maior flexibilidade a regra de negócio da instituição a criação de fórmulas visuais nas seguintes etapas do processo:
  + Depois da alteração da vaga;
  + Depois da seleção do aluno;
  + Depois do preenchimento da vaga;
  + Depois da aprovação do plano de atividade e
  + Depois da reprovação do plano de atividade.

Como exemplo de fórmula visual, podemos citar o envio de SMS ao aluno caso o mesmo seja selecionado ou reprovado na seleção.  
   
Importante: Para parametrizar os e-mails que serão enviados é necessário que seja cadastrado o  template em Currículo e Oferta | Acadêmico | Auxiliares | Mensagens de notificação
