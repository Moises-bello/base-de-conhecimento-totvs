---
content_hash: f5e9d55aed2b9871f2bdbc4baa76e59291170924c1f54d66f0bcf9fdb18cefe3
fetched_at: '2026-06-29T00:06:10.497180+00:00'
page_id: '203763453'
product: rm
source: tdn-rm
title: GLB0001_HABILITAR_BOTAO_SALVAR_PLANILHA_NET
type: documentation
url: https://tdn.totvs.com/display/LRM/GLB0001_HABILITAR_BOTAO_SALVAR_PLANILHA_NET
version: 5
---

# COMO HABILITAR O BOTÃO SALVAR PLANILHA EM UMA PLANILHA.NET

|  |  |
| --- | --- |
| **Produto:** | Framework |
| **Versões:** | 12.1.6 |
| **Ocorrência:** | Não é possível salvar Planilha.Net |
| **Ambiente:** | Planilha.Net |
| **Passo a passo:** | Foi criado uma Tag de permissão no perfil para Habilitar o botão Salvar da Planilha Net.  Com ela é possível Permitir/Proibir o usuário de salvar Planilhas Net  1) Acesse o RM.exe  2) Selecione o sistema: Serviços Globais    3) Acesse o menu Segurança – Perfis – Sistema: Serviços Globais – Edite o perfil desejado – Acesso a Menus    Após executada a alteração no perfil, acesse o menu Gestão – Planilha Net    Ao Permitir a opção Habilitar botão Salvar.  - A Planilha Net do tipo RM terá o seguinte comportamento:  O botão Salvar Planilha ficará habilitado    Ao editar e fechar a planilha, uma mensagem para salvar a planilha será exibida    Mensagem:  Deseja salvar as alterações na planilha?  - A Planilha Net do tipo Excel terá o seguinte comportamento:  O botão Salvar ficará habilitado    Ao editar e fechar a planilha, uma mensagem para salvar a planilha será exibida    Mensagem:  Deseja salvar as alterações na Planilha .Net?    Ao Proibir a opção Habilitar botão Salvar.    -  A Planilha Net do tipo RM terá o seguinte comportamento:  O botão Salvar Planilha ficará desabilitado    Ao editar a planilha e sair, uma mensagem será exibida:    Mensagem:  Usuário sem permissão para editar planilha. Os dados não serão salvos.  Se necessário utilize a funcionalidade "Salvar como Excel" para exportar a planilha.  Deseja realmente sair?    -  A Planilha Net do tipo Excel terá o seguinte comportamento:  O botão Salvar ficará habilitado    Ao clicar no botão salvar, uma mensagem será exibida pelo RM    Mensagem:  Usuário sem permissão para editar planilha. Os dados não serão salvos.  Se necessário utilize a funcionalidade "Salvar como" para exportar a planilha.    Ao editar a planilha e sair, uma mensagem será exibida:    Mensagem:  Usuário sem permissão para editar planilha. Os dados não serão salvos.  Se necessário utilize a funcionalidade "Salvar como" para exportar a planilha.  Deseja realmente sair? |
| **Observações:** |  |

divs
