---
content_hash: 32a16756fc451a4c2632e5d162b8fbab1fc67a0819adeb4dcc095bbc5b3d4494
fetched_at: '2026-06-29T00:09:30.844796+00:00'
page_id: '425458548'
product: rm
source: tdn-rm
title: Matriz Aplicada
type: documentation
url: https://tdn.totvs.com/display/LRM/Matriz+Aplicada
version: 15
---

A matriz aplicada cria o vínculo entre o [Curso](http://tdn.totvs.com/x/Af9bGQ), , Grade e . Em todos os momentos posteriores, o sistema buscará estas informações vinculadas.

É possível vincular um centro de custo à Matriz Ofertada. O sistema considerará essa informação de acordo com o parâmetro de centro de custo, pois pode ser por TURMA ou por MATRIZ APLICADA.  
   
Além do centro de custo, é possível informar o departamento no qual essa matriz aplicada pertence. Este campo não está relacionado a nenhum centro de custo.  
   
Para cada matriz aplicada da Instituição é configurado um período de matrícula. Esta configuração é feita a cada período letivo  
   
**Default contábil:** Defaults contábeis são as indicações das contas contábeis que poderão ser buscadas nos eventos contábeis. As permissões de (inclusão, edição, exclusão) dos defaults contábeis estão relacionadas às respectivas permissões de (inclusão, edição e exclusão) do cadastro de matriz aplicada.

**Oferta ativa para a matrícula:** Parâmetro responsável por habilitar/desabilitar a disponibilização da matriz aplicada durante o processo de matrícula.

A partir da versão **12.1.2406**, foi incluído o parâmetro **oferta ativa**, ao marcar a matriz aplicada fica disponível para ser vinculada a uma oferta, assim esta matriz fica disponível para realizar a parametrização por curso e a criação de turma e turma/disciplina.

Ao desmarcar o parâmetro o sistema desabilita esta matriz aplicada.

Para realizar a associação é necessário que o status da [matriz curricular](https://tdn.totvs.com/display/LRM/Matriz+Curricular) seja Ativa ou Atual. Para a [matriz curricular](https://tdn.totvs.com/display/LRM/Matriz+Curricular) inativa o parâmetro oferta ativa fica desabilitado, impossibilitando a utilização desta matriz aplicada.

## Registro de Diploma por Outra IES

A partir da versão 12.1.32 será possível informar na matriz aplicada se o registro do diploma é registrado por outra IES, pois nem todas as IES podem registrar diplomas, dependendo de outras para executar essa tarefa. Após o registro a IES registradora devolve informações para a IES de emissão que precisa armazenar essa informação e consulta-la posteriormente.

Este campo irá impactar diretamente na geração de **Diploma** no sistema. Para mais informações sobre o módulo de diplomações / certificações .

No anexo Campus polo da matriz aplicada é possível definir a disponibilidade do Campus Polo.

Apartir da versão 12.12406 foi criado o parâmetro ativo para verificar quais estão disponíveis para realizar o vinculo com a oferta/Matricula.

Por default o campo Ativo ao realizar o cadastro é habilitado.

Ao desmarcar o parâmetro o Campus/Polo em questão é inativado. Assim no curso habilitação do aluno o campus não é exibido. O mesmo ocorre para os cadastros da turma e turma disciplina.

**Observação!**Caso já tiverem com o campus/polo vinculado antes da desativação, ele permanece vinculado.

Informações Complementares

---

[Documentos exigidos - Matriz Aplicada](http://tdn.totvs.com/x/GvxbGQ)

[Tabela de Preço da Matriz Aplicada](http://tdn.totvs.com)
