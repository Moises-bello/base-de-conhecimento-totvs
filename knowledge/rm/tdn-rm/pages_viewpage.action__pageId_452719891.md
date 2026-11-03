---
content_hash: f5949241857fab1f5b645b21fdb49eba5a7c95cb88d3833fae2f270d83cfcb2b
fetched_at: '2026-06-29T00:10:10.607966+00:00'
page_id: '452719891'
product: rm
source: tdn-rm
title: Parâmetros RH
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=452719891
version: 1
---

**Parâmetros RH**   
Estes parâmetros são para definir máscaras para os cadastros que são comuns na Gestão de RH.  
   
   
**Pasta Seção**   
   
**Máscara de código de Seção**  
A máscara de seção a ser definada, servirá para padronizar os códigos de seções que serão cadastradas.  
**Exemplo**  
Ao colocar uma máscara ##.##, o sistema irá permitir a inclusão apenas para código de seção numérico, como 01.01.  
   
**Atenção**  
O campo máscara de seção será obrigatória. Caso o usuário não tenha cadastrado este campo em sua base de dados, deverá faze-ló logo que acessar o sistema.Ele deverá preencher o campo Máscara de código de seção conforme estrutura do cadastro de seções, veja exemplo abaixo:  
**Exemplo**  
01 Matriz  
01.01 Depto pessoal  
01.02 Depto.Contábil  
02 Filial Rio de Janeiro  
02.01 Depto pessoal  
02.02 Depto Contábil  
   
Neste caso, a máscara informada deverá ser = ##.##  
   
**Código de quebra mestre**  
   
Informe, aqui,o código de quebra mais utilizado, que será assumido como padrão pelo sistema. Em qualquer relatório que não for informada a quebra, o RM Labore irá considerar o código de quebra mestre.  
   
**Código de quebra para CNPJ**  
   
Informe um código de quebra de forma a refletir as quebras desejadas de seções para os fins de totalizações em relatórios e lançamentos no sistema.   
**Utiliza CEI**  
Habilite este campo apenas se a empresa utilizar o CEI (Cadastro Especial de INSS).   
**Código de quebra para CEI**  
Caso o campo anterior tenha sido selecionado, informe a quebra para CEI, usando o mesmo critério.  
   
**Pasta Máscaras dos Parâmetros Globais**   
   
**Máscara para CEP**  
Se existir alguma máscara neste campo, toda ocasião que o usuário for cadastrar qualquer endereço, o sistema irá considerar o CEP cadastrado de acordo com a máscara definida para o CEP.  
**Máscara para Telefone**  
Se existir alguma telefone neste campo, toda ocasião em que usuário for cadastrar um novo telefone, o sistema irá considerar o telefone cadastrado de acordo com a máscara definida para o telefone.  
Observação   
Os caracteres utilizados para estas máscaras são os mesmos válidos para a máscara de seção.  
   
   
**Pasta Financeiro dos Parâmetros Globais**   
   
**Código Clientes / Fornecedores**  
   
Esta Máscara irá consistir do código digitado ao realizar a inclusão de Clientes / Forncedores em cadastros | clientes/fornecedores. Vale lembrar, que esta pasta só será apresentada caso o usuário não tenha o RM Fluxus instalado, e sem cessão de uso para este sistema.  
A edição deste campo não será permitida quando já houver máscara e cliente/fornecedor cadastrados.  
Quando não houver uma máscara mas já existirem cliente/fornecedor, a edição será permitida, sendo que ao final será validado todos os registros de cliente/fornecedor com a máscara inserida, esta nova máscara somente será aceita se ela for válida para todos os registros de cliente/fornecedor.  
É bom lembrar que o cliente tem a opção de colocar uma máscara abrangente, que atenda todos os registros de cliente/fornecedor cadastrados, ou corrigir alguns códigos de fornecedores e colocar uma máscara mais restritiva, esta só poderá ser feita via script, pelo próprio cliente ou por uma customização.
