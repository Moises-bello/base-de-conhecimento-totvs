---
content_hash: 45c90dd5cdb9024877cd7f2c5a757f8fe2b9bb0c9218816177594000cbf5f303
fetched_at: '2026-06-29T00:11:18.111390+00:00'
page_id: '683360831'
product: rm
source: tdn-rm
title: Relatórios - Informe de IR
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=683360831
version: 8
---

### Introdução

---

Este relatório retorna os valores pagos por uma fonte pagadora (locatário) e recebidos pelo beneficiário (locador), de acordo com o Ano Calendário selecionada na geração do relatório.  
Para que os valores da coluna rendimentos sejam apresentados, os contratos precisam estar associados à um contrato de administração.  
Quando o imóvel não é de terceiros, subentendemos que o beneficiário é a própria coligada do imóvel.

### Procedimentos para importação

---

* Primeiramente, devemos importar nosso relatório para o banco de dados, utilizando o menu Gestão / RM Reports
* Em RM Reports, selecionar: *Processos / Importar Estrutura de relatório.*
* Na tela que se abre, selecionar o botão *"Adicionar Objetos"* e pesquisar pelo relatório *TCGIRELALG0097 - Informe Imposto Renda.TotvsReport*
* Caso seu SGBD seja Oracle, utilize o relatório TCGIRELALG0095 - Informe Imposto Renda\_ORACLE.TotvsReport
* Por padrão o diretório se encontra na pasta **ObjetosGerenciais/Relatórios** da sua instalação do RM, que por padrão é *C:/TOTVS/RM.Net/ObjetosGerenciais/Relatórios*

Importante: Caso esteja na versão 12.1.2205, o relatório está disponibilizado automaticamente na interface do TOTVS Compartilhamento. Para entender como importar o relatório para a base, siga os procedimentos neste link →  

### Procedimentos para utilização

---

Antes de utilizar o relatório, temos que dar permissão ao menu de relatórios.

Para fazer isso, siga os passos abaixo:

* Acesse *Serviços Globais / Perfil;*
* Selecione o perfil adequado e dê a permissão correta na aba Acesso a Menus;
* A permissão se encontra em *Gestão de Imóveis / Aluguel / Relatórios / Informe IR*

Para gerar o relatório de IR, vá ao menu *Aluguel/Relatórios/Informe IR.*

Selecione o relatório clicando nos três pontinhos da tela que se abre.

Após o relatório estar selecionado, identifique o cliente/fornecedor que pode ser um locatário ou locador.

Serão listados todos os imóveis, alugados no ano, divididos por fontes pagadoras e separados mensalmente. Importante frisar que:

* Quando um locatário é selecionado, somente ele será listado como fonte pagadora, podendo ser apresentados vários imóveis com vários beneficiários diferentes, mas somente de uma fonte pagadora.
* Quando um locador é selecionado serão listados todos os imóveis onde ele participou como locador no ano calendário, independente da fonte pagadora.

### Campos do relatório

---

O relatório está dividido em três seções, além do cabeçalho. Segue uma explicação mais detalhada sobre os mesmos.

Cabeçalho: Contem as informações gerenciais, como nome da coligada, título do relatório, ano calendário e contagem de páginas.

1. Beneficiário do rendimento: Apresenta o nome e CPF / CNPJ do beneficiário, ou seja, o locador.
2. Fonte Pagadora: Apresenta o nome e CPF / CNPJ da fonte pagadora, ou seja, o locatário.
3. Rendimentos.

* + Mês: Mês do pagamento e rendimento;
  + Pagamento: Valores pagos pelo imobiliário a título de aluguel;
  + Recebimento: Valores recebidos (rendimentos) repassados ao locador;
  + Total: Total dos pagamentos e recebimentos no ano calendário.
