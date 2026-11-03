---
content_hash: bae7b0b857e4e10a3e7bdc058fa944f1325eca05ecb2634d33e162090cc0d577
fetched_at: '2026-06-29T00:09:26.734969+00:00'
page_id: '423938394'
product: rm
source: tdn-rm
title: Tipos de Objeto de Manutenção (Exemplo)
type: documentation
url: https://tdn.totvs.com/pages/viewpage.action?pageId=423938394
version: 2
---

Nesta janela você poderá cadastrar os tipos de objetos de manutenção que poderão ser atendidos pelo sistema. Veja a descrição dos campos presentes da pasta Identificação e o procedimento de como preenchê-los:  
 **Código**: Código Identificador para o tipo de objeto de manutenção.

**Descrição**: Descrição do tipo de objeto de manutenção.

**Descrição no Plural**: Como será a descrição do tipo de objeto de manutenção no plural.

**Indicador de Uso**: Determina qual a unidade do indicador de uso que o tipo do objeto irá assumir.

**Nome do 1º Identificador do Objeto**: Informe o nome que será utilizado pelo sistema para o campo que contém o identificador de cada objeto de manutenção. O nome escolhido para o campo será utilizado no cadastro de Objetos de Manutenção.

**Nome do 2º Identificador do Objeto**: Nome do segundo identificador do objeto. Alguns tipos de Objeto de Manutenção podem ser controlados por dois Identificadores, daí a necessidade de um segundo Identificador.

Exemplo*:*  
 Veículos podem ser controlados por dois identificadores, como Chassi e Placa do Veículo.  
 **Máscara do 1º e 2º Identificadores**: Para padronizar o preenchimento do 1º e 2º Identificador do Objeto de Manutenção, você poderá utilizar máscaras de dados. Cada caractere da lista de regras representa um resultado de máscara diferente nos Identificadores do Objeto de Manutenção. Basta preenchê-los no campo das máscaras de acordo com as regras listadas em "Instruções da Máscara".  
Essas máscaras deverão ser criadas preenchendo os campos "Máscara 1º Identificador" e "Máscara 2º Identificador", utilizando os caracteres listados abaixo:  
 **2º Identificador do Objeto Obrigatório?**: Marcando essa caixa, será obrigatório o preenchimento do 2º Identificador sempre que você cadastrar um novo Objeto de Manutenção, em Cadastros | Objetos de Manutenção.  
 **Caixa Múltiplos Indicadores de Uso**: Os Indicadores cadastrados em Opções | Parâmetros | Gerais serão exibidos neste local. Marque o checkbox daqueles que você utilizará para este tipo de objeto de manutenção.  
***Observação:***Tipos de objetos com indicadores de uso diferentes não poderão ser considerados como Pai e Filho, impossibilitado a agregação na Pasta Filhos, no cadastro de objetos de manutenção.

Exemplo*:*  
 Um veículo cadastrado com indicador de uso "quilômetro" e um pneu com indicador de uso "mês". Neste caso não será permitido que o pneu seja tratado como Filho do Objeto-Pai veículo.  
 **Apropriação direta de produto(s)?**: Define que o objeto terá apropriação direta de produtos. Mais detalhes no "Veja Também". 

**Ícone**: Você pode acrescentar uma imagem que se associa a este Tipo de Objeto de Manutenção.  
 Na pasta Campos e Tabelas Opcionais você poderá incluir campos opcionais (numéricos e alfanuméricos) dentro das tabelas de Objetos de Manutenção, de acordo com a particularidade de cada objeto e a necessidade da empresa que utiliza o sistema.
