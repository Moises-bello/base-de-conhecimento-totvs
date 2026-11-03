---
content_hash: d31048b4bc88687300954312d7256008740f3f963001ef9e0c8707efcc0816a3
fetched_at: '2026-06-29T00:09:55.013045+00:00'
page_id: '445674427'
product: rm
source: tdn-rm
title: TCC - Educacional
type: documentation
url: https://tdn.totvs.com/display/LRM/TCC+-+Educacional
version: 9
---

---

**Parâmetros |15.07 – TCC| TCC 1/2| Parâmetros gerais**

****-**Permitir aceite do aluno para conclusão de reunião de acompanhamento**:  
Utilizado para que os acompanhamentos registrados tenham um aceite do aluno para serem considerados encerrados.

****-**Exibir os participantes da banca para o aluno no portal:**  
Utilizado para que sejam exibidos para o aluno no portal os participantes da banca.

****-**Enviar versão final dos trabalhos para os participantes da banca:**  
Utilizado para enviar o arquivo final do trabalho do TCC à todos os participantes da banca, inclusive o aluno e o Orientador.

****-**Permitir orientações acima do máximo cadastrado para o professor:**  
Utilizado para que os professores possam ser orientadores além da quantidade permitida nas configurações na visão: Orientadores por período letivo.

****-**Relatório do aceite da publicação do trabalho final**  
Visualizado pelo aluno no momento em que ele definir que seu trabalho pode ser publicado.

****-**Situação do TCC (Padrão):**  
Utilizado para informar a situação padrão do TCC. Exemplo: Em andamento, Finalizado. Etc.

****-**Situação de matrícula em disciplina:**  
Após mudar a Situação do Trabalho TCC (que indica desistência), o sistema irá mudar a automaticamente a situação de matrícula da Turma/Disciplina de TCC (onde a mesma está configurada como: Indica Disciplina como TCC).

## Parâmetros|15.07 – TCC| TCC 2/2 | Parâmetros gerais

**Armazenamento dos arquivos**

**- Tipo de armazenamento:**A forma como os arquivos postados serão armazenados.

**- Diretório de armazenamento:**Endereço do servidor onde os arquivos ficarão armazenados.

**- Tamanho máximo de armazenamento:**  
O tamanho máximo permitido (Kb) para os arquivos postados.

**- Extensões de arquivos permitidas (Exemplo: pdf,ppt):**  
São extensões permitidas para os arquivos.

falseIMPORTANTE!!!

**Para as Versões 12.1.34 e anteriores.**  
Se a Instituição de ensino, tiver parametrizado o tipo de Armazenamento como: "Arquivo de algum diretório" e informar um diretório para armazenamento, o mesmo será exclusivo para os arquivos que envolve a rotina de TCC ( Trabalho de Conclusão de Curso).

falseIMPORTANTE!!!

**A partir da Versão 12.1.2209**

Se a Instituição de ensino, tiver parametrizado o tipo de Armazenamento como: "Arquivo de algum diretório" deverá ser informado o **nome do diretório** (caso estiver com **multitenant habilitado**) ou o **caminho do diretório**(caso estiver com o **multitenant desabilitado**).

**Exemplo**quando o **multitenant**estiver **habilitado**: Imagens\Documentos → esse é o nome do diretório e subdiretório onde os arquivos serão salvos. *Não colocar caminho de pasta  →  ex: c:\arquivos.*

Referência: [Configuracao das Tags FileServerPath e LogPath](https://tdn.totvs.com/display/LRM/Configuracao+das+Tags+FileServerPath+e+LogPath)

**Exemplo**quando o **multitenant**estiver **desabilitado**: C:\Imagens\Documentos → esse é o caminho do diretório e subdiretório onde os arquivos serão salvos.
