---
content_hash: 9ad59a844b6efdbaccc47d41cbd544f801b9b30805dfbf083f377c88504ee889
fetched_at: '2026-06-29T00:09:33.309980+00:00'
page_id: '425458967'
product: rm
source: tdn-rm
title: Categorias do Processo Seletivo
type: documentation
url: https://tdn.totvs.com/display/LRM/Categorias+do+Processo+Seletivo
version: 6
---

O cadastro de categoria de processo seletivo está localizado no item "Tabelas auxiliares" e é controlado por filial.  
A categoria é utilizada como filtro de segurança no processo seletivo para cada usuário/perfil. Com isto será possível filtrar os processos seletivos tanto no aplicativo quanto no portal através de suas categorias.

**Impactos**  
No cadastro de processo seletivo existe o campo "categoria do processo seletivo", onde o cliente poderá associar as categorias pré-cadastradas e defini-las em seus processos seletivos, porém este campo não é obrigatório.  
Nos parâmetros do sistema, em "Serviço - Gerar URL" quando necessário gerar uma "URL" categorizada, basta selecionar a categoria desejada e gerar a "URL". Assim, ao acessar o portal do processo seletivo através do link gerado, será visualizado os processos seletivos da(s) categoria(s) selecionada(s).  
No cadastro de Segurança do usuário/perfil, foi disponibilizada uma nova tabela de processo seletivo (SPSPROCESSOSELETIVO) no serviço de filtro (anexado) por usuário/perfil. Desta forma o cliente poderá definir que grupos de usuários/perfis terão acessos a quais categorias de processos seletivos. Por consequência disso, todas as tabelas e cadastros filhos/anexos do processo seletivo categorizado, terão a aplicação do filtro por usuário/perfil em suas consultas.  Se o usuário/perfil não possuir este filtro, irá acessar todos os dados da filial logada como acontece atualmente.

**Exemplo**  
O serviço de inscrições é cadastro anexo (filho) do processo seletivo, portanto, quando um usuário logar no sistema e o mesmo possuir filtro para acessar somente processos seletivos da categoria "X", consequentemente a visão de inscrições que estará disponível será das inscrições pertencentes ao processos seletivos da categoria "X".

Informações Complementares

---
