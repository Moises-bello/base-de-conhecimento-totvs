---
content_hash: f990a50eb4b5374a45d47bc1aa527987ec6c36717dc3f9935337b6b99cc7acc5
fetched_at: '2026-06-29T00:11:36.488858+00:00'
page_id: '772810581'
product: rm
source: tdn-rm
title: Acelerar Relatório para o Smart View
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=772810581
version: 9
---

# Introdução

---

         O objetivo dessa página é mostrar como acelerar relatórios criados no **RMReports** para o **Smart View.**

false

# Acelerar Relatório

---

**1 -** Na visão do RMReports, selecione o relatório e clique em **Processos →Acelerar Relatório para o  Smart View.**

Para uma conversão bem sucedida, é necessário que antes de efetuar esse passo, a geração do relatório no RMReports tenha sido concluída com êxito.

**2 -** Marcando a opção "Deseja guardar uma cópia do arquivo de exportação gerado?" é possível salvar o arquivo no dispositivo. Em seguida é necessário selecionar o local onde o arquivo será exportado e clique em Executar.

**3 -** Após concluir a execução do processo, o arquivo de extensão **.treports**estará na pasta de destino com o nome do relatório.

**4 -**Acessando o Smart View, é possível ver o relatório acelerado.

false

# Geração da ON Dinâmica

---

        Após a exportação do relatório, a ON Dinâmica do mesmo é inserida na tabela **GBUSINESSOBJECTSDYNAMIC**, contendo o ID que pode ser utilizado para fazer requisições nas [API's de integração do provedor nativo](https://tdn.totvs.com/pages/viewpage.action?pageId=702351774). 

false

# Importação do Relatório no Smart View

---

Ao concluir a aceleração, também é realizado o mapeamento do recurso na [Visão de Recursos no Smart View](https://tdn.totvs.com/pages/viewpage.action?pageId=742217288). Assim, o relatório é salvo na tabela **GTREPORTSRESOURCES**. No entanto, também é possível importar o arquivo do relatório salvo anteriormente, no Smart View, e realizar outro mapeamento caso necessário. Para saber sobre importação de recursos no menu Smart View acesse .

1 - Para visualizar o arquivo exportado no Smart View, é necessário realizar sua importação. Para isso, acesse o Smart View e clique em importar relatórios e selecione o relatório exportado anteriormente. Para saber mais sobre importação/exportação de relatórios no Smart View [clique aqui](https://tdn.totvs.com/pages/viewpage.action?pageId=656818523#Exporta%C3%A7%C3%A3o/Importa%C3%A7%C3%A3odeRelat%C3%B3rios-Importa%C3%A7%C3%A3o).

2 - Após seguir o processo de importação com êxito, é possível visualizar o relatório adicionando os parâmetros necessários.

Índicefalsefalse

**Produto:** Framework

false

**Versão:** 12.1.2402

false

**Processo:** Integração com o

falsefalseStatus

YellowEM DESENVOLVIMENTO
