---
content_hash: 68ef74f6974cb0f8b529e6fb463cfaf2cba2814ad8cf7e8a10b3321690d47f25
fetched_at: '2026-06-29T00:09:32.350721+00:00'
page_id: '425458831'
product: rm
source: tdn-rm
title: Atividades Curriculares - EDU
type: documentation
url: https://tdn.totvs.com/display/LRM/Atividades+Curriculares+-+EDU
version: 8
---

Atividades curriculares são atividades cursadas pelos  que não fazem parte da grade de atividades ofertadas pela IES (Instituição de Ensino Superior) em questão.

***Exemplo:*** um aluno que cursa Sistemas de Informação participou da palestra "*Universo Java expandindo sem parar*" em outra instituição de ensino.  Analisando o diploma de comparecimento, a secretaria aceitou como válido e cadastrou em seu registro na atividade curricular deste aluno.  
   
***Importante:*** a diferença entre atividade curricular e atividade ofertada diz respeito à oferta dessas. A atividade curricular é ofertada por outra instituição e a  é concedida pela IES.  
   
São consideradas atividades curriculares cursos, seminários e palestras ofertadas por outra instituição de ensino. Essas têm como objetivo, complementar a carga horária exigida pela  grade curricular. Já que toda matriz possui um mínimo de atividades extra curriculares que devem ser cursadas para a conclusão do curso em questão.  
   
O cadastro da atividade curricular é feito no cadastro do aluno em: *Currículo e Oferta* *>*  *> Anexo >* *> Anexo > Atividades Curriculares.*   
   
Neste local é possível visualizar tanto as atividades ofertadas em que o aluno realizou suas inscrições, quanto as atividades curriculares. O que caracteriza a diferença entre elas é que as atividades curriculares do aluno não possuem o parâmetro 'Atividade ofertada pela instituição' marcado.

## Duplicidade de inscrição do Aluno

A partir das versões 12.1.31.282, 12.1.32.229, 12.1.33.160 e 12.1.34 o cadastro manual de atividade curricular do aluno passa a perguntar ao usuário se deseja duplicar a inscrição do aluno caso o mesmo já esteja inscrito. Duas validações distintas são feitas, a primeira é se a atividade ofertada pela instituição estiver vazia e a modalidade e componente preenchidos o sistema irá validar se exista alguma outra inscrição deste aluno com este mesmo componente e modalidade, caso exista uma mensagem de confirmação para o usuário será exibida o informando que o aluno já está inscrito e se deseja prosseguir, caso afirmativo, o aluno será inscrito novamente, caso negativo a inscrição não será processada. Já a segunda validação é quando a atividade ofertada pela instituição é preenchida, neste caso a validação irá ocorrer apenas para inscrições do aluno que tenha a mesma atividade ofertada pela instituição preenchida, caso exista, uma mensagem de confirmação será exibida, sendo que o usuário poderá prosseguir ou não com a inscrição duplicada.

Vale lembrar que no processo que faz inscrição de vários alunos na atividade ofertada esta mesma validação ocorre, entretanto, existe um parâmetro no processo que permite a duplicação ou não.

|  |  |
| --- | --- |
|  | Informações Complementares |

---

[Horário de Atividade Curricular](http://tdn.totvs.com.br/pages/viewpage.action?pageId=425458677)
