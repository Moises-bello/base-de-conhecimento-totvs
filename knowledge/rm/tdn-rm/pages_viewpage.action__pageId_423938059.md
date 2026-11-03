---
content_hash: 0f41389a8ef8fb0b001a605df24daed89973b534c5fab31daffc260dc48dfbf9
fetched_at: '2026-06-29T00:09:25.204135+00:00'
page_id: '423938059'
product: rm
source: tdn-rm
title: Geração de Etiquetas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938059
version: 4
---

Nessa tela são apresentadas as ordens de produção em status "Pronta para Iniciar", que estão disponíveis para a Geração de Etiquetas de Código de Barras, as etiquetas geradas aqui, após realizada a impressão , serão lidas na tela de Apontamento de Código de Barras.  
O processo de Gerar Etiquetas grava as informações na tabela Etiquetas Código de Barras (KAPTOCODBARRAETIQUETAS).   
Sendo assim para imprimir as etiquetas deve-se utilizar os novos relatórios migrados para a plataforma .NET (TOTVS Reports) para realização de Apontamento via Código de Barras.   
Os relatórios foram reformulados visando atender as novas funcionalidades desse tipo de apontamento e os mesmos encontram-se disponíveis na pasta Objetos Gerencias do diretório de instalação TOTVS (\CorporeRM\ObjetosGerenciais\Relatórios). São eles:

| Tipo de Apontamento | Descrição | Extensão |
| --- | --- | --- |
| FACREL0001 | Código de Barras por ATIVIDADES | SQL.TotvsReport |
| FACREL0002 | Código de Barras por ATIVIDADES | ORACLE.TotvsReport |
| FACREL0003 | Código de Barras por ESTRUTURA | SQL.TotvsReport |
| FACREL0004 | Código de Barras por ESTRUTURA | ORACLE.TotvsReport |
| FACREL0005 | Código de Barras Razões de Parada | SQL.TotvsReport |
| FACREL0006 | Código de Barras Razões de Parada | ORACLE.TotvsReport |
| FACREL0007 | Código de Barras Índices de Registro de Produção | SQL.TotvsReport |
| FACREL0008 | Código de Barras Índices de Registro de Produção | ORACLE.TotvsReport |
| FACREL0009 | Código de Barras por ATIVIDADES Unificado | SQL.TotvsReport |
| FACREL0010 | Código de Barras por ATIVIDADES Unificado | ORACLE.TotvsReport |

---
