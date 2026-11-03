---
content_hash: 7a45a3277915c169c4659c0ed213013a660a1d2b20133d66282424eb1d2ce44f
fetched_at: '2026-06-29T00:09:16.064552+00:00'
page_id: '421385450'
product: rm
source: tdn-rm
title: Importação e Exportação no ambiente 3 camadas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=421385450
version: 3
---

---

A configuração para exportação/importação de arquivos, consiste em copiar os arquivos gerados para uma pasta compartilhada em um servidor, podendo ou não ser copiado para uma máquina local. Para isso, é necessário informar nos Parâmetros Gerais do sistema um caminho de rede a ser utilizado pelo módulo. O caminho deve estar compartilhado, com permissão de leitura e escrita, para os usuários de rede que terão permissão de acesso para exportação/importação de arquivos. Depois de informado o caminho de rede, é necessário que o usuário acima, que possua permissão total, esteja configurado no RM.Host.Service , localizado nos Serviços do Windows em Painel de Controle | Ferramentas Administrativas | Serviços. Essa configuração permite que, ao exportar, os arquivos serão copiados para a pasta compartilhada no Servidor e em seguida para o caminho local escolhido pelo usuário no momento da exportação/importação.

**Observação:**

Em situações como o Backup/Restore do Projeto, caso a opção "Transferir arquivos gerados para o diretório de destino" estiver selecionado, no momento do processo, os arquivos de backup gerados serão copiados da pasta compartilhada do servidor para o caminho local informado pelo usuário, caso contrário, os arquivos ficarão salvos no servidor. Para mais informações veja em Backup/Restore.

**Atenção:**

Não é necessário ter nenhum software instalado (exemplo: Microsoft Excel) na máquina do usuário para que este processo possa ser executado.

---
