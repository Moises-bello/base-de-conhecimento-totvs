---
content_hash: 13b297728d076e1ff861b305b753a7a00a7e5b222d96da958269a3ee85a28f01
fetched_at: '2026-06-29T00:05:54.929641+00:00'
page_id: '118883648'
product: rm
source: tdn-rm
title: Remoção de caracteres em Campos do gerador de saídas
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=118883648
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework |
| **Processo** | **:** | Gerador de Saídas |
| **Subprocesso** | **:** | Remoção de caracteres em Campos do gerador de saídas |
| **Data da publicação** | **:** | 21/03/2014 |

Abaixo segue um exemplo de como remover caracteres de um campo do tipo CPF/CNPJ como mostrado no exemplo.

Foi utilizado o campo CNPJ para demonstração, assim:

Acessando o Registro do Layout, temos o campo CNPJ que corresponde ao campo da base de dados (GCOLIGADA.CGC). Assim clicamos no Botão “Editar Propriedades Avançadas do Registro” como mostrado no Print abaixo:

É apresentada as opções de definição deste registro.

Assim selecionamos a opção “PERSONALIZADO” e na parte “EXPRESSÃO REGULAR DOS CARACTERES” colocamos o Valor “[^a-z|0-9|A-Z]”

Após isto obtemos o resultado abaixo:

**Observação: para permitir o uso de letras acentuadas e espaçamento, colocamos o valor  [^a-z|0-9|A-Z|\s|áéíóúàèìòùâêîôûãõ]**

 

**INCLUINDO O CARACTERE Ç**

Para incluir o caractere **Ç** na impressão de layout do gerador de saídas deverá ser incluido no campo: codificação do Arquivo selecionando a opção **Europa Ocidental (ISO)**

---

|  |  |
| --- | --- |
|  | **Para maiores informações:**   **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha); |
