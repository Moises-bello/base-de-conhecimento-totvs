---
content_hash: 210536aba6b695b8ba7e047909ea2a987292b66b87a9f2d834544a1754b67c8b
fetched_at: '2026-06-29T00:05:56.970383+00:00'
page_id: '160105866'
product: rm
source: tdn-rm
title: Inserir imagem da coligada através de consulta SQL em relatório .NET
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=160105866
version: 2
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                         **Versão:**11.xx |
| **Processo** | **:** | Imagem |
| **Subprocesso** | **:** | Imagem em relatório .NET |
| **Data da publicação** | **:** | 05/09/2014 |

**Inserir imagem da coligada através de consulta SQL**

 Adicione a consulta SQL abaixo no cadastro de consultas e adicione a mesma no relatório.

***select b.IMAGEM***  
 ***from GCOLIGADA a, GIMAGEM b***  
 ***where a.IDIMAGEM = b.ID***   
 \_GoBack ***and a.codcoligada = 1***   
   
   
 Insira um componente Imagem no relatório e configure a Ligação de Dados a opção de "Imagem".

   
   
 Desta forma ao gerar relatório será visualizado a imagem da coligada.

 

---

Para maiores informações:

Icon

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
