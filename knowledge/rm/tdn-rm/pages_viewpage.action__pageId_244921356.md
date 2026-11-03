---
content_hash: d027eeeac488a610050de4036c226b39fdcd853f9262697264c02f3f497b4a3d
fetched_at: '2026-06-29T00:08:15.706356+00:00'
page_id: '244921356'
product: rm
source: tdn-rm
title: RMPAT00001_Grupos_de_Patrimônio
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=244921356
version: 10
---

# Assunto

|  |  |
| --- | --- |
| **Produto:** | TOTVS GESTÃO PATRIMONIAL |
| **Versões:** | 12.1.15. ou superior |
| **Ocorrência:** | Grupos de Patrimônio |
| **Ambiente:** |  |
| **Passo a passo:** | Responsável por agrupar patrimônios fazendo com que todas as informações e parametrizações definidas neste grupo possam ser aplicadas a cada patrimônio associado a ele.  Ao solicitar a inclusão de um novo Grupo de Patrimônio deve ser preenchida a aba de Identificação, sendo que os campos Código do Grupo e Descrição (campo livre) são obrigatórios. O Título amarrado e Taxa default são parametrizações importantes, porém, opcionais.  Amarrando um título ao grupo de patrimônio no campo **Título Amarrado** o sistema irá preencher o grupo automaticamente, quando realizado cadastros de patrimônios vinculados aquele título.  Informando o campo **Taxa default**, ao cadastrar um patrimônio informado este Grupo de Patrimônio o sistema irá informar automaticamente esta taxa para o patrimônio.    **Disponível em: Cadastros | Grupo de Patrimônio.**        Após salvar o cadastro, na aba Identificação será habilitado o **Default Contábil**, além de uma nova aba chamada **"Default Cenário/Grupo Patrimonial"** será apresentada.  Acesse Default Cenário/Grupo Patrimonial, clique em 'Incluir' e deverá ser inserido o Cenário de Cálculo e os Eventos Contábeis que este cenário irá utilizar. Perceba que para uma ocorrência, depreciação, contabilização e transferência ser executada corretamente, é necessário realizar vínculos entre Cenário, Cálculo, Evento Contábil e Grupo de Patrimônio.  Cadastros | Grupo de Patrimônio | Editar grupo | Aba Default Cenário/Grupo Patrimonial | Incluir.      Será apresenta uma aba Cenário Default para o grupo | Incluir,  informe os Eventos Contábeis correspondente a este Grupo de Patrimônio.  Após informar os Eventos Contábeis e Cenário de Cálculo correspondente | Clicar em SALVAR, em seguida o sistema irá apresentar um nova aba: **Grupo de Contas**.  Esta aba é responsável por apresentar os valores das contas correspondentes nos relatórios **(Agrupamento por contas / Contabilização / Depreciação)**.        No **Default Contábil** (**disponível na aba Identificação**) é possível informar as contas que irão compor as contabilizações de depreciação e [ocorrências](https://tdn.totvs.com/pages/viewpage.action?pageId=444596526) (baixa, acréscimo ou transferência monetária) e informações tais como, Filial, Departamento, entre outros.      O Default Contábil será utilizado caso o Item do Evento esteja parametrizado da seguinte forma: **Origem da Conta:**Tabela Default **Buscar default em:** Grupo de Patrimônio.  Qualquer processo realizado no patrimônio está diretamente ligado ao correto preenchimento da aba**'Default Cenário/Grupo Patrimonial'**, pois nesta tela será definido os Cenários de Cálculo default para o grupo.  **Exemplo:** Cadastrar Grupo de Patrimônio: 01- TESTE  Este grupo de patrimônio foi associado o cenário 01- Cenário de Cálculo Padrão, dentro deste inserido Eventos Contábeis de Aquisição, depreciação. |
| **Observações:** | Antes de excluir um Grupo de Patrimônio deve-se conferir se existe algum patrimônio cadastrado utilizando este grupo, além disso verifique se há informações cadastradas no Default Contábil, Default Cenário/Grupo Patrimonial e [campos complementares](https://tdn.totvs.com/pages/viewpage.action?pageId=423938336). Caso haja, deve-se excluir primeiro estas informações e depois o grupo de patrimônio. |
