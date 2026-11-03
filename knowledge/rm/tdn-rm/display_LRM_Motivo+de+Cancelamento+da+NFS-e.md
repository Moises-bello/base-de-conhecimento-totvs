---
content_hash: 746d0e84fd3a67d659f2440c9753bc4eb8e70a2ab133e5b173555980e760eb31
fetched_at: '2026-06-29T00:10:58.085264+00:00'
page_id: '603122182'
product: rm
source: tdn-rm
title: Motivo de Cancelamento da NFS-e
type: documentation
url: https://tdn.totvs.com/display/LRM/Motivo+de+Cancelamento+da+NFS-e
version: 9
---

Alguns municípios necessitam justificar o cancelamento de NFS-e, informando código e o motivo.

Cada município pode utilizar códigos diferentes para justificar o cancelamento.

Foi criado um cadastro onde é possível vincular ao município desejado os motivos de cancelamento da NFS-e.

Para acessá-lo basta seguir os passos:

false1true1Passo 1

Acesse:

**BackOffice | Gestão Fiscal | Cadastros | Globais (Mais) | Municípios**

Execute o filtro que retorne o município desejado e vá em:

**Anexos | Motivo de Cancelamento da NFS-e**

Imagem2Passo 2

Na tela de Motivo de Cancelamento da NFS0-e podem ser incluídos os motivos referentes ao cancelamento da nota.

No exemplo abaixo, motivos cadastrados para o município de Belo Horizonte - MG

Imagem

Caso possua algum **Motivo de Cancelamento** cadastrado no anexo do município, ao realizar o **cancelamento da NFS-e o sistema irá apresentar a tela para selecionar o motivo de cancelamento.**

ImagemInformações ImportantesfalseCampos1630416799068\_-189504484

| CAMPO | TIPO | TAMANHO | OBRIGATÓRIO |
| --- | --- | --- | --- |
| CÓDIGO | ALFANUMÉRICO | 15 | SIM |
| MOTIVO | ALFANUMÉRICO | 255 | SIM |

falseObservações

O Cadastro é feito por município;

O Cadastro é Global (não depende da Coligada);

Podem existir Códigos e Descrições iguais;

falsePermissões

O Perfil associado ao usuário precisa ter acesso na permissão **[01.02.02.04.05] Motivo de Cancelamento da NFS-e** 

Para dar esta permissão basta acessar:

**Serviços Globais | Segurança | Perfil**

**Sistema****:** Gestão Fiscal

Editar o perfil desejado e na aba **Acesso**:

**Permitir Acesso** do Motivo de Cancelamento

Imagem

Não é permitido selecionar notas de municípios diferentes para realizar o cancelamento no mesmo processo.

Necessário executar a marcação 'LI.2021.03\_03' na base de dados.

Disponível a partir da Biblioteca 12.1.32
