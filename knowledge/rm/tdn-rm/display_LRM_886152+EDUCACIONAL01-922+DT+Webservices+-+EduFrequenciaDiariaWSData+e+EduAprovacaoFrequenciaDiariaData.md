---
content_hash: 23e94f694909de7b3bb54f917adb77a4ee03dc9f5fce22654f5b619247d6313e
fetched_at: '2026-06-29T00:08:34.664536+00:00'
page_id: '274831250'
product: rm
source: tdn-rm
title: 886152 EDUCACIONAL01-922 DT Webservices - EduFrequenciaDiariaWSData e EduAprovacaoFrequenciaDiariaData
type: documentation
url: https://tdn.totvs.com/display/LRM/886152+EDUCACIONAL01-922+DT+Webservices+-+EduFrequenciaDiariaWSData+e+EduAprovacaoFrequenciaDiariaData
version: 101
---

# WEBSERVICES - EDUFREQUENCIADIARIAWSDATA E EDUAPROVACAOFREQUENCIADIARIADATA

|  |  |
| --- | --- |
| **Linha de Produto:** | *RM* |
| **Segmento:** | *Educacional* |
| **Módulo:** | *Totvs Educacional* |
| **Função:** | *Webservices - EduFrequenciaDiariaWSData e EduAprovacaoFrequenciaDiariaData* |
| **Situação/Requisito:** | *Ao executar via webservice o dataserver EduAprovacaoFrequenciaDiaria ocorre o seguinte erro: "Os dados da tabela SFREQUENCIA não foi encontrada!".* |
| **Solução/Implementação:** | *Ajuste nos dataservers EduAprovacaoFrequenciaDiaria e EduFrequenciaDiariaWSData para o seguinte funcionamento:*  *>> EduFrequenciaDiariaWSData*  *- Para dar ausência para o aluno deverá se utilizar o SaveRecord com a tag PRESENCA igual a A, sendo obrigatório a SFREQUENCIA, AlunosFreq e PARAMS. Conforme link: <http://tdn.totvs.com/x/BuP7DQ.>*  *- Para dar presença (alterar de ausência para presença) para o aluno deverá se utilizar o SaveRecord e o mesmo padrão citado acima porém com a tag PRESENCA igual a P. Com isso o sistema vai entender e remover o dado da SFREQUENCIA.*    *>> EduAprovacaoFrequenciaDiariaData*  *- O xml do SaveRecord é possível obter pelo ReadView deste DataServer.;*  *- Para disponibilizar a frequência (marcar o check "Frequência disponível no portal") sem obrigatoriedade de digitação/marcação de alguma ausência será necessário a tabela SFREQUENCIA, porém suas tags não serão preenchidas. E a tag FREQUENCIADISPWEB deverá estar preenchida com 1;*  *- Para retirar a disponibilização da frequência (desmarcar o check "Frequência disponível no portal") sem obrigatoriedade de digitação/marcação de alguma ausência será necessário efetuar o mesmo acima porém a tag FREQUENCIADISPWEB deverá estar preenchida com 0;*  *- Para atribuir um abono a uma ausência do aluno é necessário a tabela SFREQUENCIA (preenchida) e a tag JUSTIFICADA deverá estar preenchida com 1;*  *- Para remover um abono a uma ausência do aluno é necessário a tabela SFREQUENCIA (preenchida) e a tag JUSTIFICADA deverá estar preenchida com 0.*    *>> Em ambos os casos não será possível utilizar o DeleRecord, sendo que ao tentar utilizar o sistema retornará uma exceção:*  *> EduFrequenciaDiariaWSData*  *Não é possível utilizar o DeleteRecord do dataserver EduAprovacaoFrequenciaDiariaData.*  *- Se for remover frequência do(s) aluno(s) utilize o SaveRecord do dataserver EduFrequenciaDiariaWSData, porém é necessário informar a tag PRESENCA igual a P;*  *- Se for remover abono do(s) aluno(s) utilize o SaveRecord do dataserver EduAprovacaoFrequenciaDiariaData, para isso é necessário a tabela SFREQUENCIA e a tag JUSTIFICADA igual a 0;*  *- Se for remover a disponibilização da frequência no portal utilize o SaveRecord do dataserver EduAprovacaoFrequenciaDiariaData, para isso é necessário preencher a tag FREQUENCIADISPWEB igual a 0, que está presente na "PlanoAulaFreq".*    *- EduAprovacaoFrequenciaDiariaData*  *Não é possível utilizar o DeleteRecord do dataserver EduFrequenciaDiariaWSData.*  *- Se for remover frequência do(s) aluno(s) utilize o SaveRecord do dataserver EduFrequenciaDiariaWSData, porém é necessário informar a tag PRESENCA igual a P.* |
| **Conversores e Parâmetros:** | *N/A* |
| ****Tickets relacionados**:** | *N/A* |
| **Requisito (ISSUE):** | *N/A* |

divs
