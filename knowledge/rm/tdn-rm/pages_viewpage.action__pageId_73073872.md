---
content_hash: ea19039cddfc641a6116ba2f103b00fa0a7f6f3ac9b32ce7d09bd8d8f37bbbc1
fetched_at: '2026-06-29T00:11:28.287709+00:00'
page_id: '73073872'
product: rm
source: tdn-rm
title: Criando Relação de Funcionários por Dependentes.
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=73073872
version: 4
---

|  |  |  |
| --- | --- | --- |
| **Produto** | **:** | Framework                         **Versão:**11.82 |
| **Processo** | **:** | Report |
| **Subprocesso** | **:** | Relação de Funcionários por Dependentes. |
| **Data da publicação** | **:** | 25/07/2013 |

O objetivo desse exemplo, é aprender algumas funções básicas entre o Grupo Principal e grupos internos.

Com isso, vamos gerar o relatório de funcionários e seus respectivos dependente. O funcionário que não possui nenhum dependente, automaticamente não será gerado no relatório.

1. Criar um novo relatório e entre no layout.
2. Clique em Adicionar fonte de dados e insira as seguintes tabelas:  
   1. PFUNC  (Funcionário)
   2. PFDEPENDE (Dependente do Funcionário)

Exemplo:

3. No relatório, já estará disponível a linha de detalhe 1 (Detalhe 1). Insira os campos Chapa e Nome do funcionário.

4. Insira o grupo  SubDetalhe 1  interno a detalhe 1: 

5. Insira o campo PFDEPEND.NOME (Nome do dependente) no grupo Subdetalhe 1. Lembrando que será apresentado o Detalhe 2, porém este é o vínculo com o subdetalhe1

Se gerarmos o relatório neste momento, nota-se que todos os funcionários serão apresentados, mesmo que não tenham dependentes.

Para configurar de forma automática o resultado onde os funcionários que não possui dependente em seus cadastros não aparecerão na relação, devemos efetuar a seguinte configuração:

Nas propriedades da linha Detalhe 1, altere a opção DADOS > NUMERO DE IMPRESSÃO para 0 (zero) .

Salve o relatório e visualize novamente.

Note na figura acima, note que os funcionários 00008 Zelia  e 00010 Antonio não foram gerados.

|  |  |
| --- | --- |
|  | **Para maiores informações:**  Consulte o [WikiHelp TOTVS](http://wikihelp.totvs.com.br/WikiHelp/Adm/VersaoAtual.aspx)    **COMUNIDADE **[@FRAMEWORK](https://totvs.byyou.com/?space=rframework)****    **Canais de Atendimento:**  **Chamado:** Através do Portal Totvs [www.suporte.totvs.com.br](http://www.suporte.totvs.com.br/)  **Telefônico:** 4003-0015 Escolhendo as opções 2 – (Software), 2 – (Suporte Técnico), 3 – (RM), 9 – (Demais Áreas), 4 – (BI) e 3 –  (Gerador de Relatórios e Planilha). |
