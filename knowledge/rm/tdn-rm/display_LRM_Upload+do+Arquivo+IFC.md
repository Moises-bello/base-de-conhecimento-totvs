---
content_hash: 4b2feb8d5872c3c8c67ff0c6eda302b78342409042a144fd661949ef12bff0ca
fetched_at: '2026-06-29T00:10:46.891851+00:00'
page_id: '556385805'
product: rm
source: tdn-rm
title: Upload do Arquivo IFC
type: documentation
url: https://tdn.totvs.com/display/LRM/Upload+do+Arquivo+IFC
version: 13
---

---

Através do novo Menu criado “BIM”, acessando “Modelos do Projeto”, o usuário tem a possibilidade de importar este arquivo IFC com todas as propriedades da modelagem 3D e ter uma visualização dos objetos, observem:

*Para conseguir executar o processo abaixo deve-se obrigatoriamente criar uma pasta para onde os Arquivos importados possam ser gerados e informar a seguinte TAG no arquivo **RM.Host.Service.exe.config** do sistema:*

*<add key="**FILESERVERPATH**" value="Caminho da pasta" />*

*Caso existam vários servidores deve ser informado um caminho único de rede onde serão armazenados os arquivos IFC.*

Ao abrir a funcionalidade indicada, existe um processo “Upload de arquivo IFC”.

Dentro deste processo é possível definir e visualizar alguns campos:

* **Identificador do Modelo:** Campo preenchido automaticamente;
* **Disciplina:** Identifica se o Modelo IFC a ser importado é dos tipos: Arquitetura, Estrutura, Hidráulico, Elétrico ou outros;
* **Arquivo IFC:** Preenchido automaticamente com o Arquivo selecionado;
* **Descrição do Modelo:** Descrição para o arquivo IFC importado;
* **Template de Criação da EAP:**Template que será utilizado para geração da EAP automática a partir do upload do Arquivo IFC;
* **Tipo de Planilha:**Planilha onde a EAP automática será gerada.
* **Calcular dimensões dos objetos pela geometria**: Calcula as dimensões dos objetos pela geometria do modelo 3D e cria as seguintes propriedades do grupo "TOTVS":
  + Altura (caixa delimitadora)
  + Largura (caixa delimitadora)
  + Espessura (caixa delimitadora)
  + Volume
  + AreaFrontal (caixa delimitadora)
  + AreaLateral (caixa delimitadora)
  + AreaSuperior (caixa delimitadora)
* **Salvar as propriedades no banco de dados para visualização Web**: Indica se deve salvar as propriedades no banco de dados para visualização no portal minhas inspeções / diário de obra.
  + Atenção: marcar este parametro pode afetar o desempenho de arquivos IFC grandes.
* **Gerar log de trace**: Gera um arquivo de log para identificar problemas de desempenho no processo de upload.

Propriedades da TOTVS geradas no arquivo IFC após o processo de upload:

Após upload os Modelo 3d do projeto estarão disponíveis na visão de Modelos 3D:

[Voltar](https://tdn.totvs.com.br/display/LRM/Modelos+de+Projeto)
