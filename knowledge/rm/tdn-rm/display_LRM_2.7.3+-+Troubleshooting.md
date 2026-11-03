---
content_hash: b81442f980e88be6d263c7dc6cdfe980bc59a72bb46858119af39f852a17625d
fetched_at: '2026-06-29T00:11:43.527274+00:00'
page_id: '807996472'
product: rm
source: tdn-rm
title: 2.7.3 - Troubleshooting
type: documentation
url: https://tdn.totvs.com/display/LRM/2.7.3+-+Troubleshooting
version: 3
---

## Os componentes WinForms não renderizam totalmente na tela

### Sintoma

##### Tela não renderiza totalmente os componentes

##### Arquivos bloqueados pelo Windows

### Resolução

Para a resolução do problema é necessário desbloquear as DLL's da pasta TestFlow, possivelmente o windows está bloqueando o download de arquivos.

Siga os seguintes passos:

1. Pressione as teclas "windows + R" e digite o comando "gpedit.msc"
2. Na esquerda expanda as pastas para "Configuração do Usuário" >  "Modelos Administrativos" > "Componentes do Windows" > "Gerenciador de Anexos" e abra o item "Não preservar informações de zona em anexos de arquivo"
3. Altere o checkbox de "Não configurado" para "Habilitado" e, em seguida, pressione "Aplicar" e "OK"
4. Baixe novamente os plugins através do TestFlow
5. Extraia o zip instalado no diretório do RM.exe

Após a execução dos passos os componentes WinForms serão carregados por completo.
