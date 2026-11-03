---
content_hash: 9f2da9bef91891828c9b5939c42c38c46126adee58118a3233596bcaa22ab193
fetched_at: '2026-06-29T00:05:58.820403+00:00'
page_id: '189303349'
product: rm
source: tdn-rm
title: Boletim Técnico - Integração RM x GED com ECM e Fluig
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=189303349
version: 6
---

|  |  |  |
| --- | --- | --- |
| **Produto** | : | RM Integração 11.82 |
| **Processo** | : | Boletim Técnico - Integração RM x GED com ECM e Fluig |
| **Data da publicação** | : | 25/05/15 |

## Contexto de negócio (Introdução)

O sistema eletrônico de gestão de documentos (GED) da Totvs possui um sistema de integração entre os sistemas RM com ECM ou RM com Fluig.   
 Esta integração permite ao usuário postar documentos diretamente do RM nos sistemas ECM e Fluig de maneira transparente, respeitando todas as regras de mapeamento de diretórios, permissões de acesso, leitura e escrita.   
 O sistema GED permite aos clientes que fazem uso das várias ferramentas de gestão da Totvs gerenciarem seus documentos de forma integrada e contextual ao seu negócio, economizando tempo, processo e trabalho de seus usuários.

## Sistemas Envolvidos

* RM/Integração – Possui todas as funcionalidades e parametrizações para integrações do RM com diversos sistemas
* ECM/GED – Gestão Eletrônica de Documentos do ECM
* Fluig/GED – Gestão Eletrônica de Documentos do Fluig

## Integração

Clientes que fazem uso do RM e do ECM ou Fluig sentiram a necessidade de integrar a gestão eletrônica de documentos contextual ao negócio. Desta forma, o RM criou um processo de integração que permite o envio de documentos pelo RM para o ECM ou Fluig.

## Escopo

Todos os usuários podem utilizar a integração GED com ECM ou Fluig, bastando ter as permissões necessárias para acionar a função de Anexo de uma visão.   
 Esta integração permite ao usuário mapear qual diretório ECM ou Fluig a publicação de documentos estará destinada. Isto permite ao usuário publicar arquivos no RM para o ECM ou Fluig, bem como alterá-lo ou excluí-lo.   
 Todos os arquivos que serão publicados pelo RM nesta integração são destinadas às pastas mapeadas e estas pastas devem possuir as permissões necessárias do usuário publicador.   
 Como a publicação de arquivos utiliza o protocolo de comunicação FTP, é necessário que a configuração do ECM ou Fluig seja feita em comum acordo com a parametrização do RM para que a integração funcione sem problemas de infra-estrutura, como inconsistência de endereçamentos, portas e nomes de usuários.

## Pré-requisitos instalação/implantação/utilização

* Versões mínimas dos produtos
  + RM: 11.82.36
  + ECM: 3.0.0
  + Fluig: 1.0.0
* É necessária a parametrização dos dados de integração no módulo de Integração do RM
* É necessária sincronização de usuários RM com usuários ECM ou Fluig para publicação de documentos
* É necessária configuração de permissão de acesso aos diretórios do GED no ECM ou Fluig
* É necessário que as configurações de permissão de acesso estejam devidamente setadas na rede para comunicação com o RM na integração
* O RM deve estar instalado em uma máquina Windows em arquitetura 2 ou 3 camadas
* O Fluig deve ser instalado em uma máquina que possua um dos seguintes sistemas operacionais  
  + Windows Server 2008 R2 ou superior
  + Linux RedHat Enterprise 6.4 ou superior
  + Linux Oracle 6.4 ou superior
* O ECM deve ser instalado em uma máquina que possua um dos seguintes sistemas operacionais  
  + Windows Server 2008 R2 ou superior
  + Linux SUSE 10 ou superior
  + Linux Ubuntu 11 ou superior
  + Linux RedHat 6 ou superior

## Instalação/Atualização

* A parametrização no RM para integração GED com os produtos ECM ou Fluig deve ser realizada no Módulo Integração, Guia Ferramentas, Menu Parâmetros e selecionar na listagem de parametrizações o item Linha RM x GED
* Para casos em que a integração seja com o Fluig, a opção Integração Fluig deve ser marcada e a matrícula do Usuário de Integração deve ser fornecida
* Quando a porta para FTP for diferente da padrão (20 ou 21) nos servidores do ECM ou Fluig, estes devem ser informados na parametrização no campo Porta FTP
* O RM precisa estar na versão de release 11.82.36 ou superior
* Na estrutura dos sistemas ECM e Fluig existe um diretório utilizado para fazer o upload dos arquivos do RM através do FTP. É necessário dar permissão de escrita nesta pasta (no ambiente ECM ou Fluig) para o Usuário de Integração utilizado na parametrização da integração conseguir fazer o upload pelo FTP

## Controle de Versão

O grupo TOTVS representado por suas marcas irá administrar as demandas de evolução dos layouts e demais ajustes, acordando junto aos solicitantes o prazo de liberação de release.   
 Todas as evoluções programadas deverão ser discutidas e aprovadas pelas marcas antes do início do desenvolvimento e somente serão desenvolvidas em caso de concordância das marcas e alinhamento com as diretivas definidas pelo Comitê de Integração TOTVS.

## Suporte

O suporte aos recursos da Integração será de responsabilidade de todas as linhas, sendo assim as equipes de suporte dos produtos RM, ECM e Fluig estarão aptas a fazer a primeira análise e, quando necessário, repassar para a equipe mais adequada em cada caso.

## Fluxo das Informações

* Após instalação do ECM ou Fluig, aciona-se a opção de Sincronização de Usuários do RM. Esta opção criará os usuários correspondentes aos existentes no RM no ECM ou Fluig
* Com os usuários sincronizados, é necessário criar os diretórios no ECM ou Fluig e definir os níveis de acesso, permissão de leitura e escrita.
* Após criados diretórios no ECM ou Fluig, será necessário mapear o diretório de escrita no RM
* Com o diretório mapeado, basta acessar o menu Anexos em qualquer visão para publicar um arquivo no GED.

## *Checklist* de suporte da aplicação

* Verificar se o Servidor, Porta e Usuários estão configurados corretamente na parametrização da integração GED
  + Se for Fluig, verificar se a matrícula do usuário está correta também
  + Faça um ping no endereço para verificar se o servidor está disponível para acesso
* Verificar se a Matrícula do usuário ECM ou Fluig está correspondente ao campo USERID do usuário RM
* Fazer uma conexão FTP utilizando um software de terceiros (Filezilla por exemplo)
  + Fazer upload de arquivos também
* Perguntar para o suporte do ambiente ECM ou Fluig se a pasta utilizada para upload de arquivos por FTP está com permissão de escrita do usuário de integração informado na parametrização
* Verificar se as portas de FTP são diferentes das padrões
  + Caso sejam, identificar interrogando os responsáveis pela infra-estrutura se a rota de comunicação está liberada nestas portas entre os ambientes RM e ECM ou Fluig
* Coletar evidências do mau funcionamento relatado pelo cliente

Para maiores informações:

Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/GLB/GLB.Perfis.aspx)

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha).
