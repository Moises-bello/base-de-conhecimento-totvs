---
article_id: 360024769093
category: Atualização
content_hash: 0151e3e7d6a086f31a00f22716b697a579e91d90d03cd97b58b510b7dd8f5d49
fetched_at: '2026-06-28T22:42:21.246587+00:00'
product: protheus
section_id: 360000076747
source: central-protheus
title: Framework - Linha Protheus  - Iniciar 2 instâncias do CtreeServer no mesmo
  Servidor
type: support-article
updated_at: '2024-05-08T11:10:05Z'
url: https://centraldeatendimento.totvs.com/hc/pt-br/articles/360024769093-Framework-Linha-Protheus-Iniciar-2-inst%C3%A2ncias-do-CtreeServer-no-mesmo-Servidor
---

**Dúvida**  
É possível iniciar 2 instâncias do CtreeServer em um mesmo Servidor?  
  
**Ambiente**Protheus - AppServer - Todas as versões  
  
**Solução**  
Sim, é possível. Para iniciar 2 instâncias no mesmo Servidor, siga o procedimento abaixo:  
  
1. Pare o serviço do Ctree Server atual;  
2. Crie uma cópia do diretório base FairCom;  
3. Altere o nome desta cópia para FairCom2;  
4. Acesse a pasta FairCom2\V9.5.2\winX64\bin\ace\isam;  
5. Editar o arquivo CTSRVR.CFG alterando a linha SERVER\_NAME:  
; Server Name  
SERVER\_NAME FAIRCOMS2 -> Colocar um novo nome da segunda instalação do Ctree Server  
  
6. Incluir a linha SERVER\_PORT:  
; Server Name  
SERVER\_NAME FAIRCOMS2   
SERVER\_PORT 5001 -> Colocar uma nova porta  
  
7. Salve o arquivo;  
8. Crie um serviço com o comando **sc create** via CMD, conforme exemplo abaixo:  
sc create nome\_do\_serviço binPath= "C:\FairCom2\V9.5.2\winX64\bin\ace\isam\ctsrvr.exe"  
  
9. Inicie o serviço criado;  
10. Altere no arquivo appserver.ini do Protheus:  
[CTREESERVER]  
CTUSERID=ADMIN  
CTUSERPASS=ADMIN  
CTSERVER=FAIRCOMS2@LOCALHOST -> O mesmo nome colocado no CTSRVR.CFG do Ctree Server.  
  
Observação: a porta padrão do Ctree Server é a 5597.
