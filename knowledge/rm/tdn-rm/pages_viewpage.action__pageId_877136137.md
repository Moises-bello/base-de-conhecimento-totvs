---
content_hash: 6f46cebd0a254898cacb3edd3c730989417257e9630631cf53196aa293ef25c4
fetched_at: '2026-06-29T00:11:59.909723+00:00'
page_id: '877136137'
product: rm
source: tdn-rm
title: Pré-Venda - Pessoas - DTA Vision Document
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=877136137
version: 17
---

### **Introdução**

---

A partir do **Release 12.1.2410** o sistema permite o uso da ferramenta de IA, ***DTA Vision Document***, para executar a a extração de dados do *[Prospect](https://tdn.totvs.com/pages/viewpage.action?pageId=701668855)*, a partir dos arquivos de documentos, por meio do botão *Extrair Dados de Doc.*

### Procedimentos para utilização

---

Para utilizar a funcionalidade, basta acessar a visão de prospects, editar ou criar um novo prospect e clicar no botão correspondente:

Ao clicar no botão "Extrair Dados de Doc o sistema exibe as orientações abaixo, já na interface do DTA Vision Document. Leia com atenção e avance para a próxima tela.   
Ao marcar a opção "Não exibir a mensagem de boas-vindas novamente" a funcionalidade irá diretamente para a interface de upload de documentos, tornando o processo mais ágil.

O DTA Vision Document tem as seguintes recomendações:

* ***Tamanho de arquivo suportado: Até 2MB;***
* ***Imagem legível e na horizontal;***
* ***Documentos suportados: PNG, JPEG, JPG WEBP e PDF.***

Na tela seguinte, é apresentada a opção para continuar a sessão em um celular ou tablet, através da leitura do QR Code desta sessão e também as opções para envio dos documentos, através do seu tipo.

As opções disponíveis são:

* ***Documento de Endereço;***
* ***Carteira de Motorista;***
* ***Registro Geral / Carteira de de Identidade.***

O sistema realizará o OCR (reconhecimento de texto) dos documentos de acordo com a sua característica, preenchendo automaticamente os dados (campos) na visão de prospect que forem achados pela ferramenta. Lembrando que o DTA Vision é um facilitador e os documentos precisam estar legíveis e sem perdas para a correta extração. 

### Sobreposição de Dados Existentes no Upload de Documentos

---

Ao realizar o upload de documentos no cadastro de pessoas, o sistema permite ao usuário decidir como os dados extraídos desses documentos devem ser tratados: **sobrepondo** ou **Preenchendo dados flatantes** nas informações já existentes no sistema.

### Como Funciona:

Antes de preencher os dados no cadastro, o sistema verifica se já existem informações salvas para aquela pessoa. Se houver, ele realiza uma comparação entre os **dados atuais do sistema** e os **dados extraídos do novo documento enviado**.

Se forem detectadas diferenças, o sistema exibirá uma tela com duas opções:

* **Sobrepor**
* **Preencher dados faltantes**

Junto com essas opções, será exibida uma lista com os dados divergentes, mostrando lado a lado:

* **Valor Atual** (o que já está cadastrado no sistema)
* **Novo Valor** (o que foi lido no novo documento)

O usuário então escolhe se deseja **substituir todos os dados atuais divergentes** (**Sobrepor**) ou apenas **completar os campos que ainda estão em branco** (**Preencher dados faltantes**).

*A substituição ou preenchimento será feita para todos os campos listados.  
Não é possível escolher individualmente quais campos deseja substituir ou preencher.**Se não houver nenhuma diferença entre os dados atuais e os novos, essa tela não será exibida, e o sistema entenderá que não há necessidade de substituição.*

### Opções Disponíveis

* **Sobrepor**  
  Todos os campos divergentes serão atualizados com os dados do novo documento, substituindo os valores atuais do cadastro.
* **Preencher dados faltantes**  
  Apenas os campos que estão **vazios** no cadastro atual serão preenchidos com os dados do novo documento. Campos já preenchidos não serão alterados, mesmo que o novo valor seja diferente.

Essa funcionalidade funciona tanto para **cadastros novos** quanto para **cadastros já existentes que estejam sendo editados**.

### Exemplo Prático:

Imagine que você cadastrou uma pessoa chamada **João Silva**, com os seguintes dados:

* **Nome**: João Silva
* **Endereço**: Rua das Flores, 123
* **Telefone**: *(vazio)*

Agora, você realiza o upload de um novo documento que contém:

* **Nome**: João A. Silva
* **Endereço**: Avenida Central, 456
* **Telefone**: (77) 9123-5555

Você poderá então escolher:

* **Sobrepor**: Todos os campos serão atualizados com os novos valores.  
  O cadastro ficará como:

  + Nome: João A. Silva
  + Endereço: Avenida Central, 456
  + Telefone: (77) 9123-5555
* **Preencher dados faltantes**: Apenas o campo **Telefone** será preenchido, pois os demais já tinham valores.  
  O cadastro ficará como:

  + Nome: João Silva *(mantido)*
  + Endereço: Rua das Flores, 123 *(mantido)*
  + **Telefone: (77) 9123-5555 *(preenchido)***

**Prioridade no preenchimento de dados da Pessoa com Múltiplos documentos**

---

Quando uma pessoa envia mais de um documento ao mesmo tempo (como carteira de motorista, carteira de identidade e documento de endereço), o sistema escolhe qual documento usar para preencher cada tipo de dado.

#### **Como funciona a prioridade:**

* A carteira de motorista (CNH) tem a maior prioridade.
* A carteira de identidade (RG) é usada caso a CNH não esteja presente.
* O documento de endereço é usado apenas para preencher o endereço e telefone.

#### Importante: Os campos como **nome, CPF e data de nascimento** **nunca** devem ser preenchidos ou sobrescritos por informações do documento de endereço. **Exemplo Prático:**

Imagine que uma pessoa envia os seguintes documentos juntos:

* Carteira de motorista com nome "João Silva", CPF "123.456.789-00"
* Documento de endereço com nome "João da Silva", telefone "(11) 99999-9999", e endereço "Rua A, 123"

#### O que o sistema faz:

* **Nome e CPF** são preenchidos com os dados da **carteira de motorista**:  
  → Nome: João Silva  
  → CPF: 123.456.789-00
* **Endereço e telefone** são preenchidos com os dados do **documento de endereço**:  
  → Endereço: Rua A, 123  
  → Telefone: (11) 99999-9999
* O nome "João da Silva" do documento de endereço é ignorado, pois a prioridade é da CNH.

Sempre que houver documentos de identificação (CNH ou RG) e um documento de endereço juntos, o sistema preenche os dados da pessoa com base nos documentos de identificação, e usa o documento de endereço apenas para endereço e telefone.

* Importante ressaltar, que a funcionalidade do *DTA Vision Document* apresenta um tempo máximo de sessão que é de 10 minutos.
* Após clicar em enviar, será possível fechar para conferir os dados importados e se necessário retornar a esta sessão e enviar novos do documentos.
* Ao término deste processo, sugerimos que a sessão seja finalizada acionando o botão destinado a este fim.
* A funcionalidade de OCR ou reconhecimento de texto, pode apresentar erros de extração dada a qualidade dos documentos enviados. Sempre **confira todos os dados** antes de salvar o prospect no sistema.
