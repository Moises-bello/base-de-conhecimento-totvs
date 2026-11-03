---
content_hash: 015f40199f22556cd9f48947a6a029a05a761f644c1de2b5431a0ae5bf0d7b5c
fetched_at: '2026-06-28T21:35:28.773172+00:00'
page_id: '695600349'
product: fluig
source: tdn-fluig
title: Atualizações (1.8.0)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=695600349
version: 457
---

## 1

## Ciclo de atualização

Maior destaque para as atualizações evolutivas (**Update**). 

As liberações mais relevantes são identificadas por um selo especial:

 **Essential:** incluem correções e pequenas evoluções da plataforma.

 **Mandatory:**atualizações que possuem correções críticas emergenciais.

Veja todos os detalhes em: [Atualização da plataforma](https://tdn.totvs.com/x/2xVbB).

oculto

240924

## 24 de Setembro de 2024

---

## Correções

FBPM-9031

* Realizada correição para corrigir a inclusão de anexos, aplicação de filtro por anexo e exclusão de anexo filtrado, dentro do processo.

240723

## 23 de Julho de 2024

---

Correção Mandatory

Foi identificada uma vulnerabilidade crítica que requer uma atenção especial em seu ambiente.  
A situação corrigida encontra-se disponível a partir do pacote **[Mandatory 1.8.0-240723](https://tdn.totvs.com/pages/viewpage.action?pageId=695600349#Atualiza%C3%A7%C3%B5es(1.8.0)-240723)**.

## Correções

* Realizado ajuste na tela de consulta de solicitações ao alterar o idioma.
* Ajuste realizado para que o menu da Store seja apresentado corretamente ao atualizar o TOTVS Fluig.
* Corrigido o gerenciamento das licenças do Fluig.
* Ajuste realizado para que não ocorra inconsistência no campo Data ao trocar o idioma da plataforma.

240313

## 13 de Março de 2024

---

## Correções

* Efetuadas correções para que os parâmetros do *link* de primeiro acesso à plataforma não sejam perdidos em um navegador onde já exista uma sessão iniciada e um novo acesso ao *link* seja feito depois de 30 minutos.
* Ajuste realizado para que a atualização entre versões do Fluig Plataforma ocorra corretamente não ocasionando inconsistências nessa atualização.

240227

## 27 de Fevereiro de 2024

---

## Correções

* Efetuadas correções no redirecionamento de URL para permitir acessar a plataforma Fluig a partir de um navegador *mobile*.
* Ajuste realizado para que ao aplicar restrição de visualização na página Store para usuários admin a mesma reflita a restrição adicionada corretamente.
* Efetuadas correções para permitir que um usuário comum possa ativar ou desativar outros usuários comuns quando possuir permissão para isso.

240109

## 09 de Janeiro de 2024

---

## Correções

* Feito tratamento para que não sejam executados *scripts* no parâmetro "errorMsg" ao chamar a URL utilizando um *payload* com códigos maliciosos, sanando vulnerabilidades e aumentando a segurança.
* Implementada biblioteca DOMPurify para auxiliar no tratamento de vulnerabilidades pelo frontend.
* Realizada correção nos aplicativos My Approval e My Fluig, para que ao acessar a central de tarefas de um usuário substituído, somente as tarefas relacionadas às quais estou designado como substituto sejam exibidas.
* Realizada correção para que a remoção de um arquivo da lixeira de outro usuário através da API interna não seja permitida.

231205

## 05 de Dezembro de 2023

---

## Correção

* Corrigida inconsistência no processo cuja tarefa possui um mecanismo de atribuição por campo de formulário (Pool:Group:Nome\_Grupo), para que ao movimentar, não apresente nenhum erro.

## 231127

## 27 de Novembro de 2023

---

Correção Mandatory

Foi identificada uma vulnerabilidade crítica que requer uma atenção especial em seu ambiente.  
A situação corrigida encontra-se disponível a partir do pacote **[Mandatory 1.8.0-231127](https://suporte.totvs.com/portal/p/10098/suporte-fluig-download#000035/FLUIG%201.8/Fluig/)**.

Saiba quais são os impactos:

* Esta situação permitia a exploração de *Cross-site scripting* pela página mobileredir. Foram realizados ajustes para sanar essa falha de segurança.

231031

## 31 de Outubro de 2023

---

## Correções

* Realizada correção no *style guide* que permite o use de tabelas e *tags* complementares dentro do componente *popover*.
* Realizada correção para que as solicitações não sejam apresentadas de forma duplicada na Central de Tarefas.
* Realizada correção para que o evento \_beforetasksave \_execute normalmente na transferência da solicitação.

231017

## 17 de Outubro de 2023

---

Atenção!

Informamos que as mídias liberadas entre os dias **05/09/23** a **10/10/23** estão sujeitas a apresentar inconsistências se instaladas em banco de dados Oracle. Para as novas instalações recomendamos utilizar mídias fora do intervalo mencionado.

Confira a [notícia](https://tdn.totvs.com/pages/viewpage.action?pageId=871502812#:~:text=Equipe%20TOTVS%20Fluig.-,18/10/2023,-Inconsist%C3%AAncia%20nas%20m%C3%ADdias) que divulgamos no portal do cliente.

## Correções

* Correção realizada para que ao utilizar caracteres especiais com codificação diferente em imagens, os mesmos sejam normalizados com o mesma codificação aceita pela plataforma.
* Correção realizada para que seja possível iniciar a aplicação da plataforma.
* Realizada correção no Fluig para que o botão de "Enviar imagem" seja mostrado somente quando estiver dentro de subpastas.

231010

## 10 de Outubro de 2023

---

## Correções

* Feitos ajustes em opções de  de notificação de prazo de tarefas e solicitações que estavam duplicadas.
* Realizada correção no agendador de tarefas para sanar problemas de travamento na fila.
* Realizada correção na Lista Mestra, para que o histórico de aprovação em subpastas seja apresentado corretamente.

231003

## 03 de Outubro de 2023

---

## Correções

* Ajustes realizados para otimizar a geração de [thumbnail](https://tdn.totvs.com/x/4gBlDw).

## 230926

## 26 de Setembro de 2023

---

## Melhoria

**Novo método de visualização de documentos**

Agora os documentos do tipo PNG, JPG, JPEG e BMP, por padrão, não virão com a opção de visualizador interno assinalado, permitindo assim que os documentos sejam abertos e visualizados diretamente pelo visualizador padrão do navegador.

Caso queira visualizar estas extensões via *Fluig Viewer*, será necessário assinalar a opção dentro das propriedades do documento. Acesse a  [documentação](https://tdn.totvs.com/x/kRJoDg) para saber mais detalhes.

230919

## 19 de Setembro de 2023

---

## Correção

* Criado novo dataset Interno para trazer as informações de mecanismos de atribuição. Confira mais detalhes na documentação de [Datasets internos](https://tdn.totvs.com/x/SgKeCQ).

## Melhoria

**Reajustada a quantidade de requisições da visualização de documentos**

Essa solução veio com o objetivo de reduzir as requisições desnecessárias que ocorriam quando um documento era visualizado várias vezes, pois a cada nova visualização o serviço era acionado para converter o documento.

230912

## 12 de Setembro de 2023

---

## Correções

* Realizado ajustes de segurança na API de listagem da Store.

230905

## 05 de Setembro de 2023

---

## Melhorias

**Itens da store agora é Store!**

Nessa atualização o recurso Itens da Store que você conhecia passou por mudanças e agora se chama Store - a página de soluções do TOTVS Fluig que agora está mais moderna e intuitiva.

Aprimoramos a busca por soluções reposicionando o campo de busca para a parte superior da página, proporcionando maior destaque e praticidade para você na hora de buscar por uma solução.

sample1Campo de busca

Além dos filtros já existentes, criamos novos filtros que auxiliam a encontrar as soluções de forma mais eficaz. 

Você pode acionar o filtro através do ícone  filtrar soluções por:

* + Desenvolvedor;
  + Categorias;
  + Tipo.

Além disso, organizamos as categorias separando-as por Novidades, Todas as soluções e Flows. Essa divisão torna o uso de cada categoria mais prático, permitindo que você encontre soluções específicas em categorias distintas.

sample1Categorias da store

Aproveite essa novidade e confira a nova página Store do TOTVS Fluig.

Confira mais detalhes no help [Store](https://tdn.totvs.com/x/frOcEw).

## Correções

* Efetuados ajustes na definição de permissões para que os recursos do  sejam exibidos corretamente para usuários comuns quando eles recebem permissão de acesso a esses recursos – tais como  e  – e quando o banco de dados utilizado é o Oracle.
* Realizado ajuste para que ao adicionar ou renomear um arquivo com tags no nome, não sejam interpretadas como HTML pelo Fluig.

230829

## 29 de Agosto de 2023

---

## Correções

* Realizada correção para sanar lentidão na página de configuração de processos, para que seja feita uma chamada do \_alert \_para cada API.
* Correção realizada para que seja possível localizar usuários, grupos ou papéis ao criar uma página.
* Incluído status "Finalizado" ao utilizar o componente de upload do style guide Fluig e realizado ajuste na área de upload para que fique disponível para inclusão de novos arquivos.
* Correções realizadas a fim de garantir que todos os componentes do bootstrap estejam na versão 3.4.1 e atualizado os componentes Tooltip e Popover para a versão 3.4.1-FLUIG.
* Alterada a opção ***Flags* "*HttpOnly*" e "*Secure*" nos *cookies*** para que seja habilitada automaticamente ao selecionar a opção **HTTPS** como protocolo nas .

230822

## 22 de Agosto de 2023

---

## Correções

* Aumentada a segurança da edição de campos do recurso , tanto pela página quanto pela API.
* Correção realizada para que as permissões sejam apresentadas ao utilizar o layout comunicativo para criar páginas.

230815

## 15 de Agosto de 2023

---

## Correções

* Efetuados ajustes para bloquear alterações nas preferências do usuário via API quando o usuário que está autenticado não é o mesmo que está sendo alterado, mesmo que o autenticado seja o administrador, permitindo assim, que apenas as próprias informações de quem está autenticado sejam alteradas.
* Realizada correção ao executar o importador de dados históricos, para que os campos com valores fixo em formato de texto (*String*) possam ser lidos pelo importador e enviados ao analytics corretamente.
* Realizada correção para que ao desmarcar a opção de PDF/A, os vídeos no formato .MP4 sejam exibidos corretamente.
* Realizada correção no campo zoom, para que permita consultas com maior número de caracteres.

230808

## 08 de Agosto de 2023

---

## Correções

* Correção de inconsistência ao consumir API de listagem de documentos na pasta.
* Alterada a opção de notificação "Senha alterada recentemente" para "Senha recuperada recentemente", localizada na aba Gerais da , pois essa notificação somente é emitida quando é feito o processo de recuperação de senha.
* Realizada correção na configuração das atividades, para que não seja possível inserir \_tags \_e alterar a cor da fonte.
* Realizada correção em documentos, para que ao copiar e colar uma pasta com arquivo que possuía segurança herdada, não fique em carregamento e impeça a inclusão da pasta.

230801

## 01 de Agosto de 2023

---

## Correções

* Correção realizada no comportamento do componente [checkbox](https://style.fluig.com/components.html#custom-checkbox-and-radio) dentro da tabela pai e filho.
* Corrigida API para possibilitar a ativação das notificações em comunidades.
* Realizada correção no menu de descrição principal dos registros de um formulário, para que a descrição inserida seja incluída corretamente.

## 230726

## 26 de Julho de 2023

---

Correção Mandatory

Foi identificada uma vulnerabilidade crítica que requer uma atenção especial em seu ambiente.  
A situação corrigida encontra-se disponível a partir do pacote **[Mandatory 1.8.0-230726](https://suporte.totvs.com/portal/p/10098/suporte-fluig-download#000035/)**.

Saiba quais são os impactos:

* Esta situação permitia a alteração dos dados de acesso dos usuários pela página de Preferências. Foram realizados ajustes para sanar essa falha de segurança.

## Correções

* Correção realizada para permitir a edição de campos na página de Temas ao acessar com o usuário wcmadmin.
* Correção de inconsistência no componente de zoom, para não permitir a seleção de mais de um registro.

## 230718

## 18 de Julho de 2023

---

## Melhorias

### Implementada criptografia de senha no AD

Pensando em deixar a sua segurança ainda maior, foi aplicada uma atualização no sistema, que permite agora utilizar uma senha encriptada do LDAP.

Através de uma *tag* utilizada no *domain*, será possível definir se a senha será encriptada ou não.

Para saber de todos os detalhes e como funciona esta novidade, acesse a documentação [Configuração de autenticação utilizando LDAP](https://tdn.totvs.com/x/XQVbDw). Concluída

### Melhoria no campo zoom

Sempre pensando em trazer melhorias que façam a diferença na sua rotina, trouxemos a inclusão do caractere porcento "**%**" para a pesquisa do campo zoom, a fim de melhorar a experiência e facilitar a utilização.

## Correções

* Realizada correção para que seja possível executar os comandos SQL do update em qualquer banco homologado pelo Fluig.
* Realizada correção para que seja executada a atualização da imagem docker e o sistema seja atualizado corretamente, alterando para a versão instalada.
* Realizada correção na visualização de documentos, para que ao gerar uma nova versão, seja possível visualizá-lo corretamente.
* Realizada correção para que a impressão de uma cópia controlada não apresente nenhuma inconsistência.
* Realizado ajuste para que seja possível incluir a permissão na API de resultados do processo.
* Realizada melhoria para o controle de versão no evento global.
* Correção realizada para que ao trocar o tema para o Snowflake o mesmo seja aplicado corretamente em toda a plataforma.

## 230711

## 11 de Julho de 2023

---

## Melhorias

### TOTVS Flows: Sua solicitação de compra facilitada

Já imaginou otimizar e agilizar a implantação de processos na sua empresa para facilitar o dia a dia dos seus colaboradores? Bom, isso já é possível!

Apresentamos o **[TOTVS Flows - Solicitação de compra](https://tdn.totvs.com/x/yFVzL)**. Com ele é possível abrir pedidos de compras de forma otimizada, podendo informar qual item será comprado, direcionando para as devidas aprovações da gestão e área de compras. Permitindo ainda, realizar o cadastro de itens e do centro de custo consumido no processo.

Tudo para trazer mais facilidade à sua rotina!

#e8f6f0#e8f6f0

![](https://tdn.totvs.com/download/attachments/563436139/dica.png)

**DICA!**  
Depois de instalado, o *flow* **Solicitação de compra** fica disponível como um processo no recurso [Iniciar solicitações](https://tdn.totvs.com/x/VfHuDQ), com o nome e a categoria que foram definidos na instalação.
