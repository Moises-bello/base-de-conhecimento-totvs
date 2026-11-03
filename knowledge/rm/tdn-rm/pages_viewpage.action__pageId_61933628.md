---
content_hash: a92354be33d1855d8730abab5f8a54adc0c05fb7530d165ebf4b17ecb8f6f6e9
fetched_at: '2026-06-29T00:11:02.643234+00:00'
page_id: '61933628'
product: rm
source: tdn-rm
title: Contabiliza número de páginas de impressão - Reports
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=61933628
version: 5
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | TOTVS Reports                         **Versão:**11.80 |
| **Processo** | **:** | Edição de Componente |
| **Subprocesso** | **:** | Informações da Página |
| **Data da publicação** | **:** | 11/06/2013 |

Para que o usuário possa alterar o layout do informativo que contabiliza as páginas de impressão ele deverá realizar a seguinte configuração.

        Atualmente o sistema carrega o informativo com o seguinte layout “Página 1 de 2”, “Página 2 de 2” e assim sucessivamente. Este layout default atende a seguinte formatação; Página ### de {1}

      Para alterar o layout de apresentação deste contador devemos realizar proceder da seguinte forma. Selecione o componente “Informações da Página” do final do relatório. Depois de selecionado o componente clique sobre sua smart tag.

       O sistema irá apresentar as propriedades do componente “Informações da Página”, clique sobre as reticências da propriedade “Formato”. Altere a formatação da propriedade adotando o seguinte layout; ### / {1}

       Com esta formatação teremos na impressão a contagem de página seguindo a ordem: 1 / 3, 2 / 3, 3 / 3. Abaixo veja o exemplo de como ficou esta contagem ao final de cada página na geração do relatório.

---

Para maiores informações:

**COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****

**Canais de Atendimento:**

**Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br)

**Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha);
