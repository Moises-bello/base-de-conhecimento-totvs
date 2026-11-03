---
content_hash: 423d2b14312c73b74ce85f472179591fdb381b4e7a3c00a326472a9772479b96
fetched_at: '2026-06-29T00:09:09.829903+00:00'
page_id: '394210586'
product: rm
source: tdn-rm
title: PORTALMOBILE01-5052 3418752 DT Permissão de professor para digitação de notas
  e frequência diária
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=394210586
version: 1
---

# Permissão de professor para digitação de notas e frequência diária

|  |  |
| --- | --- |
| **Linha de Produto:** | RM |
| **Segmento:** | TOTVS Gestão Educacional |
| **Módulo:** | Educacional |
| **Função:** | Frequência diária e digitação de notas |
| **Situação/Requisito:** | Ao logar com um usuário de professor, onde no seu perfil não esteja parametrizado para Coordenadores de curso permissão para digitação de frequência diária e/ou notas de etapas, o usuário de professor não tinha permissão para realizar estas alterações. Mesmo o professor não sendo coordenador, no qual estas permissões não deveriam afetar a permissão do usuário. |
| **Solução/Implementação:** | Em alguns casos o nome de usuário do professor continha um espaço no final do nome, não sendo possível validar suas permissões e tipos de usuários, quando pesquisados no banco de dados que normalmente não possuíam espaços, causando uma não identificação do professor, retirando suas permissões de acesso como professor, e identificando o professor como um Coordenador de curso, mas sem acesso, devido ao perfil de usuário. |
| **Conversores e Parâmetros:** | N/A |
| **Tickets relacionados:** | N/A |
| **Requisito:** | N/A |
| **Documento de Referência:** | N/A |
| **Pacote:** | N/A |
